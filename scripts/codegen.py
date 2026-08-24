from __future__ import annotations

import keyword
import pathlib
import re
import subprocess
import sys
import textwrap
import unicodedata

import yaml


SCALARS = {"string": "str", "integer": "int", "number": "float", "boolean": "bool"}
# Only keywords need a suffix: a field named id or type shadows nothing and
# reads better plain. Builtins are shadowed only in method signatures, so the
# suffix belongs there rather than on struct fields.
RESERVED = {"type", "filter", "format", "list", "next", "object", "bytes", "id"}


def snake(x: str) -> str:
    x = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", x)
    # Latinise first: stripping non-ASCII outright turned every Cyrillic or CJK
    # name into the same "field_", silently merging distinct fields.
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode() or _transliterate(x)
    x = re.sub(r"[^a-zA-Z0-9]+", "_", x).lower().strip("_")
    if keyword.iskeyword(x):
        x += "_"
    return x or "field_"


_CYRILLIC = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "sch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def _transliterate(x: str) -> str:
    """A Cyrillic name is worth romanising; anything else keeps its fallback."""
    return "".join(_CYRILLIC.get(c, _CYRILLIC.get(c.lower(), "")) for c in x)


def arg(x: str) -> str:
    out = snake(x)
    return out + "_" if out in RESERVED else out


def pascal(x: str) -> str:
    return "".join(p[:1].upper() + p[1:] for p in re.split(r"[^a-zA-Z0-9]+", x) if p)


def detect_pagination(query: set[str], body_props: set[str], resp_props: set[str], path: str) -> str | None:
    """Detect how an endpoint paginates."""
    if path.endswith("/count"):  # counters return a number, not a page
        return None
    if "next" in query or "next" in resp_props:
        return "next"
    if "cursor" in body_props or "cursor" in resp_props:
        return "cursor"
    if "rrdId" in body_props or "rrdid" in {q.lower() for q in query}:
        return "rrdid"
    if {"skip", "take"} <= query:
        return "skip_take"
    if "offset" in query:
        return "offset_query"
    if "offset" in body_props:
        return "offset_body"
    return None


_DATA_KEYS = ("data", "cards", "orders", "supplies", "items", "feedbacks", "questions", "result")


def _items_field(resp_props: set[str]) -> str | None:
    for key in _DATA_KEYS:
        if key in resp_props:
            return key
    return None


_HTML_TAG = re.compile(r"<[^>]+>")
_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_BLANKS = re.compile(r"\n{3,}")


def safe_doc(text: str) -> str:
    """Make text safe inside a triple-quoted string.

    Summaries sometimes end in a quote, which would merge with the closing
    quotes into a broken literal.
    """
    out = text.replace('"""', "'''")
    while out.endswith('"') or out.endswith("\\"):
        out = out[:-1].rstrip()
    return out


def wrap_doc(text: str, width: int = 96, indent: str = "    ") -> list[str]:
    if not text:
        return []
    text = safe_doc(text)
    if len(indent) + len(text) + 6 <= width:
        return [f'{indent}"""{text}"""']
    body = textwrap.wrap(text, width=width - len(indent), break_long_words=False)
    return [f'{indent}"""{body[0]}'] + [f"{indent}{line}" for line in body[1:]] + [f'{indent}"""']


def clean_doc(text: str, limit: int = 900) -> str:
    if not text:
        return ""
    out = _HTML_TAG.sub("", text)
    out = _MD_LINK.sub(r"\1", out)  # [text](link) -> text
    out = _BLANKS.sub("\n\n", out)
    lines = [line.rstrip() for line in out.split("\n")]
    # trim blank edges but keep paragraph breaks inside
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    result = "\n".join(lines).strip()
    if len(result) > limit:
        cut = result[:limit].rsplit("\n", 1)[0]
        result = cut.rstrip() + "\n…"
    return result


def indent_doc(text: str, spaces: int = 4, width: int = 104) -> str:
    pad = " " * spaces
    out: list[str] = []
    for line in text.split("\n"):
        if not line.strip():
            out.append("")
            continue
        stripped = line.lstrip()
        extra = " " * (len(line) - len(stripped))
        for part in textwrap.wrap(stripped, width=width - spaces - len(extra), break_long_words=False) or [
            ""
        ]:
            out.append(f"{pad}{extra}{part}")
    return "\n".join(out)


def _param_lines(meth: dict, kwargs: list[str]) -> list[str]:
    docs = meth.get("docs") or {}
    lines = []
    for kw in kwargs:
        attr = kw.split("=")[0]
        api_name = next(
            (n for n in docs if arg(n) == attr),
            next((p for p in meth["path_params"] if arg(p) == attr), None),
        )
        text = docs.get(api_name or "", "").strip()
        if not text:
            continue
        head = f"        :param {attr}: "
        if len(head) + len(text) <= 108:
            lines.append(head + safe_doc(text))
            continue
        wrapped = textwrap.wrap(text, width=108 - len(head), break_long_words=False)
        lines.append(head + safe_doc(wrapped[0]))
        lines.extend(f"            {part}" for part in wrapped[1:])
    return lines


# The action comes from the summary rather than the HTTP verb: Wildberries
# often uses POST for reads (order stickers, for one), so a _post suffix would
# be misleading.
# The leading verb of a summary names the action. Order matters only within a
# group; the match is anchored, so a noun later in the summary cannot win.
_ACTIONS: tuple[tuple[str, str], ...] = (
    (r"создать|создание|добавить|добавление|сформировать|генерац|присоедин|назначить", "create"),
    (r"удалить|удаление|убрать|открепить|очистить|расформировать", "delete"),
    (r"отменить|отмена", "cancel"),
    (r"загрузить|загрузка", "upload"),
    (r"закрепить|привязать|установить|задать", "set"),
    (
        r"обновить|обновление|изменить|изменение|редактировать|отредактировать|"
        r"редактирование|передать|перевести|подтвердить|объединение|перенос|"
        r"восстановление|разъединение|пересчитать",
        "update",
    ),
    (
        r"получить|получение|список|информаци|проверить|проверка|скачать|запросить|"
        r"история|статус|детализац|детали|состояние|лимит|бренды|характеристик|"
        r"отчёт|отчет|данные|поиск|найти|количество|"
        # Wildberries serves these reads over POST and titles them with a noun,
        # so the HTTP verb would name them create_*.
        r"статистика|остатки|пагинация|заказы|воронка|основная страница",
        "get",
    ),
)


_VERB_ACTION = {
    "GET": "get",
    "POST": "create",
    "PUT": "set",
    "PATCH": "update",
    "DELETE": "delete",
}

# Path segments that carry no meaning in a method name.
_NOISE = frozenset({"api", "v0", "v1", "v2", "v3", "v5", "marketplace", "adv", "info"})

# Filler WB puts mid-path (/get/cards/list, /list/goods/filter). Kept as the
# last segment, where "list" tells /offer/keys/{id}/list apart from
# /offer/keys/{id}, and "content" is the whole subject of /api/v1/content/delete.
_LEADING_NOISE = frozenset({"list", "get", "content"})


_LIMIT_ROW = re.compile(
    r"^\|\s*(?P<c1>[^|\n]*?)\s*\|\s*(?P<c2>[^|\n]*?)\s*\|\s*(?P<c3>[^|\n]*?)\s*\|"
    r"\s*(?P<c4>[^|\n]*?)\s*\|(?:\s*(?P<c5>[^|\n]*?)\s*\|)?\s*$",
    re.MULTILINE,
)
_NUM_UNIT = re.compile(r"^(\d+)\s*(мс|сек|с|мин|ч)")
_TOKEN_KINDS = {
    "персональный": "personal",
    "сервисный": "service",
    "базовый": "basic",
    "базовый с секретом": "basic_secret",
    "тестовый": "test",
}
_TO_MS = {"мс": 1, "сек": 1000, "с": 1000, "мин": 60000, "ч": 3600000}


# x-category from the spec -> bit in the token scope mask (field s).
_SCOPE_BY_CATEGORY = {
    "content": "CONTENT",
    "contentanalytics": "ANALYTICS",
    "discountsandprices": "PRICES",
    "marketplace": "MARKETPLACE",
    "statistics": "STATISTICS",
    "advert": "PROMOTION",
    "questionsandfeedback": "FEEDBACKS",
    "buyerchat": "BUYER_CHAT",
    "supplies": "SUPPLIES",
    "returns": "RETURNS",
    "documents": "DOCUMENTS",
    "finance": "FINANCE",
    "usermanagement": "USERS",
}


def parse_rate_limits(description: str) -> dict[str, tuple[int, int]]:
    """Read rate limits out of the markdown table in a method description.

    Wildberries publishes them as "Период | Лимит | Интервал | Всплеск",
    sometimes with a leading token-category column. A basic token is limited
    orders of magnitude harder, so the categories are kept apart.
    """
    limits: dict[str, tuple[int, int]] = {}
    for match in _LIMIT_ROW.finditer(description or ""):
        cells = [
            c for c in (match["c1"], match["c2"], match["c3"], match["c4"], match["c5"]) if c is not None
        ]
        if any(set(cell) <= set("- ") for cell in cells):
            continue
        kind = "all"
        if cells[0].lower() in _TOKEN_KINDS:
            kind = _TOKEN_KINDS[cells[0].lower()]
            cells = cells[1:]
        if len(cells) < 4:
            continue
        # "Период | Лимит" is the sustained rate; "Интервал | Всплеск" only
        # describes how much of it may be spent at once. Configuring the
        # limiter from the burst columns let /news run at 10 req/min where the
        # spec allows 1.
        period = _NUM_UNIT.match(cells[0])
        allowance = re.match(r"^(\d+)", cells[1])
        burst = re.match(r"^(\d+)", cells[3])
        if not period or not allowance or not burst:
            continue
        window_ms = int(period.group(1)) * _TO_MS[period.group(2)]
        permitted = int(allowance.group(1))
        if permitted < 1:
            continue
        # Scale the window rather than dividing it, so integer division cannot
        # round the rate upward: 1000 // 3 * 6 is 1998ms, slightly faster than
        # the 3 req/s the row allows.
        burst_size = int(burst.group(1))
        limits[kind] = (window_ms * burst_size // permitted, burst_size)
    return limits


def _servers_for(op: dict, item_servers: list | None, spec: dict, sandbox: bool = False) -> list[str]:
    """The endpoint hosts: production, or the sandbox ones."""
    for scope in (op.get("servers"), item_servers, spec.get("servers")):
        urls = [
            s["url"].rstrip("/")
            for s in (scope or [])
            if isinstance(s, dict)
            and isinstance(s.get("url"), str)
            and s["url"].startswith("https://")
            and ("sandbox" in s["url"]) == sandbox
        ]
        if urls:
            return urls
    return []


# Spot fixes where a Wildberries spec disagrees with what the API returns.
# Each one was confirmed against the live API.
SPEC_FIXES: dict[tuple[str, str, str], str] = {
    # Tags come back as an array, though the spec describes a single object.
    ("/content/v2/tags", "get", "data"): "array",
}


def apply_spec_fixes(path: str, verb: str, schema: dict) -> dict:
    """Apply the fixes above to a response schema."""
    properties = schema.get("properties") if isinstance(schema, dict) else None
    if not properties:
        return schema
    for (fix_path, fix_verb, field_name), shape in SPEC_FIXES.items():
        if fix_path != path or fix_verb != verb or field_name not in properties:
            continue
        if shape == "array":
            inner = properties[field_name]
            properties[field_name] = {"type": "array", "items": inner}
    return schema


def action_for(summary: str, verb: str) -> str:
    """The action a method performs, read from the leading verb of its summary.

    Anchored on purpose: an unanchored search let a noun anywhere in the
    summary decide, so "Создать отчёт" matched the get pattern on "отчёт".
    """
    low = summary.lower().strip().lstrip("«\"'")
    for pattern, action in _ACTIONS:
        if re.match(rf"(?:{pattern})", low):
            # "Добавить" makes a new thing over POST, but over PATCH it edits
            # one that already exists: adding orders to a supply.
            if action == "create" and verb == "PATCH":
                return "update"
            return action
    return _VERB_ACTION.get(verb, verb.lower())


# Words whose singular a suffix rule would get wrong.
_SINGULARS = {
    # "pass" is a keyword, so this one stays plural.
    "passes": "passes",
    "status": "status",
    "statuses": "status",
    "offices": "office",
    "boxes": "box",
    "warehouses": "warehouse",
    "taxes": "tax",
    "stickers": "sticker",
    "news": "news",
    # Not plurals, though they end like them.
    "series": "series",
    "species": "species",
    "cookies": "cookie",
    "trbx": "trbx",
    "stats": "stats",
    "settings": "settings",
    "goods": "goods",
    "meta": "meta",
}


def singular(word: str) -> str:
    """A rough singular, enough for method names."""
    if word in _SINGULARS:
        return _SINGULARS[word]
    if word.endswith("ies") and len(word) > 5:
        return word[:-3] + "y"
    if word.endswith(("ses", "xes", "zes", "ches", "shes")):
        return word[:-2]
    # Latin singulars that already end in s: status, bonus, analysis, basis.
    if word.endswith(("us", "ss", "is")):
        return word
    if word.endswith("s") and len(word) > 3:
        return word[:-1]
    return word


# Paths that carry less meaning than the endpoint does: /adv/v0/delete says
# nothing about what is deleted.
NAME_FIXES: dict[str, str] = {
    "/adv/v0/delete": "delete_campaign",
    # WB tells these apart by a singular/plural path alone.
    "/api/v1/offer/{offer_id}": "update_offer_status",
}


def _rename_refs(text: str, renames: dict[str, str]) -> str:
    """Rewrite whole-word class references, longest name first."""
    for old_name in sorted(renames, key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(old_name)}\b", renames[old_name], text)
    return text


def compose_name(path: str, action: str, section: str) -> str:
    """Build a verb-first name: create_supply, get_orders_new, set_meta_gtin."""
    if path in NAME_FIXES:
        return NAME_FIXES[path]

    # Compare on singular stems: the finances section owns /api/finance/... .
    section_words = {singular(w) for w in section.split("_")}
    parts = [
        snake(part) for part in path.strip("/").split("/") if part not in _NOISE and not part.startswith("{")
    ]
    # Split to words first: snake() has fused hyphenated segments, so
    # /normquery/get-bids arrives as one part and a per-part filter misses the
    # "get" inside it.
    words = [w for part in parts for w in part.split("_") if w]

    # Filler anywhere but last: /content/v2/get/cards/list keeps "list".
    # "get" is never the point of a path, so it goes even there.
    parts = [
        w for i, w in enumerate(words) if (i == len(words) - 1 and w != "get") or w not in _LEADING_NOISE
    ]

    # WB repeats a word across segment boundaries (/search-report/report,
    # /upload/upload-chunk); saying it twice adds nothing.
    parts = [w for i, w in enumerate(parts) if i == 0 or w != parts[i - 1]]

    # A segment equal to the action would read as cancel_cancel or
    # delete_delete; the action already carries it, at either end.
    if parts and parts[-1] == action:
        parts = parts[:-1]
    # Unless that empties the name: /api/v1/content/delete is about the content,
    # and a bare verb says nothing, so the filler word earns its place back.
    if not parts:
        parts = [w for w in words if w not in {"get", action}] or words
    if len(parts) > 1 and parts[0] == action:
        parts = parts[1:]

    # The leading segment usually repeats the section name, but it is the
    # subject in /supplies/{id}/orders, so it is dropped only from the front —
    # and only when what remains still names something specific.
    if len(parts) > 2 and singular(parts[0]) in section_words:
        parts = parts[1:]

    if action in ("create", "delete", "set", "update", "cancel") and parts:
        parts = parts[:-1] + [singular(parts[-1])]

    if not parts:
        # A path made only of placeholders leaves nothing to name the subject
        # after, and a bare verb says nothing about what it acts on.
        placeholders = [snake(seg.strip("{}")) for seg in path.strip("/").split("/") if seg.startswith("{")]
        return f"{action}_by_{placeholders[0]}" if placeholders else action

    # A keyword as the last word cannot end a method name; the plural reads
    # better than the underscore snake() would leave: get_tariffs_returns.
    # A word already ending in "s" would triple it — class, pass, is.
    if keyword.iskeyword(parts[-1]):
        last = parts[-1]
        parts = parts[:-1] + [f"{last}es" if last.endswith("s") else f"{last}s"]

    return f"{action}_{'_'.join(parts)}"


class Generator:
    def __init__(self, spec: dict, domain: str) -> None:
        self.spec = spec
        self.domain = domain
        info = spec.get("info") or {}
        self.title = (info.get("title") or domain).strip().strip("'\"")
        self.description = clean_doc(info.get("description") or "")
        self.structs: dict[str, str] = {}
        self.methods: list[dict] = []

    # ---- types ----------------------------------------------------------
    def _resolve(self, ref: str) -> dict:
        node: dict = self.spec
        for part in ref.lstrip("#/").split("/"):
            node = node.get(part, {})
        return node

    def type_of(self, sch: dict | None, hint: str, depth: int = 0) -> str:
        if not isinstance(sch, dict) or depth > 6:
            return "Any"
        if "$ref" in sch:
            target = self._resolve(sch["$ref"])
            # A component can describe a scalar or an array rather than an
            # object; only emit a struct when the reference really is one.
            if not isinstance(target, dict) or not (
                target.get("properties") or target.get("type") == "object"
            ):
                return self.type_of(target, hint, depth + 1)
            name = pascal(sch["$ref"].split("/")[-1])
            if name not in self.structs:
                self.emit_struct(name, target, depth + 1)
            return name
        for combo in ("allOf", "oneOf", "anyOf"):
            if combo in sch and isinstance(sch[combo], list) and sch[combo]:
                return self.type_of(sch[combo][0], hint, depth + 1)
        if sch.get("type") == "array":
            return f"list[{self.type_of(sch.get('items'), hint + 'Item', depth + 1)}]"
        if sch.get("type") == "object" or "properties" in sch:
            if not sch.get("properties"):
                return "dict[str, Any]"
            name = pascal(hint)
            if name not in self.structs:
                self.emit_struct(name, sch, depth + 1)
            return name
        return SCALARS.get(sch.get("type", ""), "Any")

    def emit_struct(self, name: str, sch: dict, depth: int = 0) -> None:
        self.structs[name] = ""  # placeholder that stops the recursion
        props = sch.get("properties") or {}
        if not props:
            self.structs[name] = f"class {name}(WBModel):\n    pass\n"
            return
        lines = [f"class {name}(WBModel):"]
        doc = (sch.get("description") or "").strip().split("\n")[0]
        if doc:
            lines.insert(1, f'    """{safe_doc(doc[:88])}"""\n')
        used: set[str] = set()
        for prop, ps in sorted(props.items()):
            field = snake(prop)
            while field in used:
                field += "_"
            used.add(field)
            pytype = self.type_of(ps, f"{name}{pascal(prop)}", depth + 1)
            rename = f', name="{prop}"' if field != prop else ""
            lines.append(f"    {field}: {pytype} | None = _field(default=None{rename})")
            doc = (
                clean_doc(ps.get("description") or "", 160).replace("\n", " ") if isinstance(ps, dict) else ""
            )
            lines.extend(wrap_doc(doc))
        self.structs[name] = "\n".join(lines) + "\n"

    # ---- methods --------------------------------------------------------

    def collect(self) -> None:
        self._collect_methods()
        self._resolve_name_clashes()
        self._rename_shadowed_models()

    def _rename_shadowed_models(self) -> None:
        """Keep a model from taking the name of a method class.

        Both land in the section facade, where the second import silently wins
        and the call resolves to the model instead of the endpoint.
        """
        taken = {method["cls"] for method in self.methods}
        shadowed = sorted(name for name in self.structs if name in taken)
        if not shadowed:
            return

        renames = {name: f"{name}Model" for name in shadowed}
        self.structs = {
            renames.get(name, name): _rename_refs(body, renames) for name, body in self.structs.items()
        }
        for method in self.methods:
            for key in ("return_type", "item_type"):
                if isinstance(method.get(key), str):
                    method[key] = _rename_refs(method[key], renames)

    def _resolve_name_clashes(self) -> None:
        """Separate methods that ended up with the same name.

        Two endpoints on one path occasionally mean the same thing — goods
        with prices come both as a list and by article. The id, the API
        version, or failing both the HTTP verb tells them apart.
        """
        seen: dict[str, list[dict]] = {}
        for method in self.methods:
            seen.setdefault(method["name"], []).append(method)

        for name, group in seen.items():
            if len(group) < 2:
                continue
            # /supplies and /supplies/{supplyId} collapse to the same name once
            # the placeholder is dropped, and both are GET — the id is what
            # tells them apart, so name it before falling back to the verb.
            by_id = [m for m in group if "{" in m["path"]]
            if len(by_id) == 1 and len(group) == 2:
                by_id[0]["name"] = f"{name}_by_id"
                by_id[0]["cls"] = pascal(by_id[0]["name"])
                continue

            # Two versions of one endpoint (/adv/v0/… and /adv/v1/…) share a
            # verb, so the version is the only thing that separates them.
            versions = [re.search(r"/(v\d+)/", m["path"]) for m in group]
            if all(versions) and len({v.group(1) for v in versions if v}) == len(group):
                for method, version in zip(group, versions, strict=True):
                    assert version is not None
                    method["name"] = f"{name}_{version.group(1)}"
                    method["cls"] = pascal(method["name"])
                continue

            for method in group:
                method["name"] = f"{name}_{method['verb'].lower()}"
                method["cls"] = pascal(method["name"])

    def _collect_methods(self) -> None:
        for path, item in (self.spec.get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            shared = [p for p in (item.get("parameters") or []) if isinstance(p, dict)]
            for verb, op in item.items():
                if verb not in ("get", "post", "put", "patch", "delete"):
                    continue
                if not isinstance(op, dict):
                    continue
                self.methods.append(self._method(path, verb, op, shared, item.get("servers")))

    def _method(
        self,
        path: str,
        verb: str,
        op: dict,
        shared: list[dict] | None = None,
        item_servers: list | None = None,
    ) -> dict:
        summary = (op.get("summary") or "").strip().split("\n")[0]
        name = compose_name(path, action_for(summary, verb.upper()), self.domain)
        params = list(shared or []) + [p for p in (op.get("parameters") or []) if isinstance(p, dict)]
        # shared parameters arrive as references and need resolving too
        params = [self._resolve(p["$ref"]) if "$ref" in p else p for p in params]
        params = [p for p in params if isinstance(p, dict) and p.get("name")]
        # The path placeholders are the source of truth: a spec sometimes
        # leaves them undeclared.
        declared = {p["name"] for p in params if p.get("in") == "path"}
        for ph in re.findall(r"\{(\w+)\}", path):
            if ph not in declared:
                params.append({"name": ph, "in": "path", "required": True, "schema": {"type": "string"}})
        body_sch = (
            ((op.get("requestBody") or {}).get("content") or {}).get("application/json", {}).get("schema")
        )
        responses = op.get("responses") or {}
        ok = next(
            (responses.get(k) for k in (200, "200", 201, "201") if isinstance(responses.get(k), dict)),
            None,
        )
        rsch = ((ok or {}).get("content") or {}).get("application/json", {}).get("schema")
        if isinstance(rsch, dict):
            rsch = apply_spec_fixes(path, verb, rsch)
        # An object body becomes keyword arguments: trbx_ids=[...] rather
        # than body={"trbxIds": [...]}.
        body_fields: list[tuple[str, bool, str]] = []
        body_docs: dict[str, str] = {}
        body_kind = None
        if isinstance(body_sch, dict):
            resolved = self._resolve(body_sch["$ref"]) if "$ref" in body_sch else body_sch
            props = resolved.get("properties") if isinstance(resolved, dict) else None
            if props and len(props) <= 12:
                required = set(resolved.get("required") or [])
                body_kind = "fields"
                for prop, ps in props.items():
                    body_fields.append(
                        (
                            prop,
                            prop in required,
                            self.type_of(ps, f"{pascal(name)}{pascal(prop)}"),
                        )
                    )
                    if isinstance(ps, dict):
                        body_docs[prop] = clean_doc(ps.get("description") or "", 160).replace("\n", " ")
            else:
                body_kind = "raw"

        resp_props = set()
        if isinstance(rsch, dict):
            target = self._resolve(rsch["$ref"]) if "$ref" in rsch else rsch
            resp_props = set((target.get("properties") or {}).keys()) if isinstance(target, dict) else set()
        body_props = {prop for prop, _, _ in body_fields}
        pagination = detect_pagination(
            {p["name"] for p in params if p.get("in") == "query"},
            body_props,
            resp_props,
            path,
        )

        return dict(  # noqa: C408 — named fields read better than a literal
            scope=_SCOPE_BY_CATEGORY.get(str(op.get("x-category") or "").lower()),
            rate_limits=parse_rate_limits(op.get("description") or ""),
            host=(_servers_for(op, item_servers, self.spec) or [""])[0],
            sandbox_host=(_servers_for(op, item_servers, self.spec, sandbox=True) or [""])[0],
            pagination=pagination,
            items_field=_items_field(resp_props),
            name=name,
            cls=pascal(name),
            verb=verb.upper(),
            path=path,
            summary=summary,
            path_params=[p["name"] for p in params if p.get("in") == "path"],
            query_params=[
                (p["name"], bool(p.get("required")), self.type_of(p.get("schema"), pascal(p["name"])))
                for p in params
                if p.get("in") == "query"
            ],
            docs={
                **{
                    p["name"]: clean_doc(p.get("description") or "", 160).replace("\n", " ")
                    for p in params
                    if p.get("name")
                },
                **body_docs,
            },
            body_kind=body_kind,
            body_fields=body_fields,
            body_type=self.type_of(body_sch, f"{pascal(name)}Body") if body_sch else None,
            return_type=self.type_of(rsch, f"{pascal(name)}Response") if rsch else "None",
        )

    # ---- rendering ------------------------------------------------------
    def render_types(self) -> str:
        head = [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from msgspec import field as _field",
            "",
            "from ..client.model import WBModel",
            "",
            "",
        ]
        body = [self.structs[name] for name in sorted(self.structs) if self.structs[name]]
        return "\n".join(head) + "\n" + "\n\n".join(body)

    def render_methods(self) -> str:
        out = [
            "from __future__ import annotations",
            "",
            "@TYPING@",
            "from ..client.method import WBMethod",
            "@SCOPE@",
            "@MODELS@",
            "",
            "",
        ]
        for m in sorted(self.methods, key=lambda x: x["name"]):
            docs = m.get("docs") or {}

            def _field(api_name: str, declaration: str, docs: dict = docs) -> list[str]:
                lines = [declaration]
                lines.extend(wrap_doc((docs.get(api_name) or "").strip()))
                return lines

            # Required fields must precede defaulted ones, so each group is
            # sorted on its own.
            required: list[tuple[str, list[str]]] = []
            optional: list[tuple[str, list[str]]] = []
            for p in m["path_params"]:
                required.append((arg(p), _field(p, f"    {arg(p)}: str | int")))
            if m["body_kind"] == "raw":
                required.append(("body", [f"    body: {m['body_type']} | list[Any] | dict[str, Any]"]))
            for prop, req, pt in m["body_fields"]:
                line = f"    {arg(prop)}: {pt}" if req else f"    {arg(prop)}: {pt} | None = None"
                (required if req else optional).append((arg(prop), _field(prop, line)))
            for q, req, qt in m["query_params"]:
                line = f"    {arg(q)}: {qt}" if req else f"    {arg(q)}: {qt} | None = None"
                (required if req else optional).append((arg(q), _field(q, line)))

            fields = [
                line
                for _, block in sorted(required, key=lambda x: x[0]) + sorted(optional, key=lambda x: x[0])
                for line in block
            ]
            out.append(f"class {m['cls']}(WBMethod[{m['return_type']}]):")
            out.append(f'    """{safe_doc(m["summary"])}\n')
            out.append(f'    {m["verb"]} {m["path"]}\n    """')
            out.append("")
            out.append(f'    __path__ = "{m["path"]}"')
            out.append(f'    __http_method__ = "{m["verb"]}"')
            out.append(f"    __returns__ = {m['return_type']}")
            if m["path_params"]:
                out.append(f"    __path_params__ = {tuple(m['path_params'])!r}")
            if m["query_params"]:
                qmap = {arg(q): q for q, _, _ in m["query_params"]}
                out.append(f"    __query_params__ = {qmap!r}")
            if m["scope"]:
                out.append(f"    __scope__ = Scope.{m['scope']}")
            if m["host"]:
                out.append(f'    __host__ = "{m["host"]}"')
            if m["sandbox_host"]:
                out.append(f'    __sandbox_host__ = "{m["sandbox_host"]}"')
            if m["rate_limits"]:
                out.append(f"    __rate_limits__ = {m['rate_limits']!r}")
            if m["pagination"]:
                out.append(f'    __paginate__ = "{m["pagination"]}"')
            if m["items_field"]:
                out.append(f'    __items__ = "{m["items_field"]}"')
            if m["body_fields"]:
                bmap = {arg(prop): prop for prop, _, _ in m["body_fields"]}
                out.append(f"    __body_fields__ = {bmap!r}")
            if fields:
                out.append("")
                out.extend(fields)
            out.append("")

        rendered = "\n".join(out).replace("@MODELS@", self._models_import(out))
        typing_import = "from typing import Any\n" if re.search(r"\bAny\b", rendered) else ""
        rendered = rendered.replace("@TYPING@\n", typing_import)
        scope_import = "from ..utils.token import Scope\n" if "Scope." in rendered else ""
        return rendered.replace("@SCOPE@\n", scope_import)

    def _models_import(self, lines: list[str]) -> str:
        text = "\n".join(lines)
        used = sorted(
            name for name in self.structs if self.structs[name] and re.search(rf"\b{re.escape(name)}\b", text)
        )
        if not used:
            return ""
        if len(used) == 1:
            return f"from .models import {used[0]}"
        return "from .models import (\n" + "".join(f"    {n},\n" for n in used) + ")"

    def render_facade(self) -> str:
        out = [
            "from __future__ import annotations",
            "",
            "@ITER@",
            "@TYPING2@",
            "",
            "@IMPORTS@",
            "@MODELS@",
            "",
            "",
            "if TYPE_CHECKING:",
            "    from ..client import WBApi",
            "",
            "",
            f"class {pascal(self.domain)}:",
            f'    """{self.title}.\n\n{indent_doc(self.description)}\n    """'
            if self.description
            else f'    """{self.title}."""',
            "",
            "    __slots__ = ('_api',)",
            "",
            "    def __init__(self, api: WBApi) -> None:",
            "        self._api = api",
            "",
        ]
        for meth in sorted(self.methods, key=lambda x: x["name"]):
            req_args: list[tuple[str, str]] = []
            opt_args: list[tuple[str, str]] = []
            for p in meth["path_params"]:
                req_args.append((arg(p), f"{arg(p)}: str | int"))
            if meth["body_kind"] == "raw":
                req_args.append(("body", "body: Any"))
            for prop, required, pt in meth["body_fields"]:
                decl = f"{arg(prop)}: {pt}" if required else f"{arg(prop)}: {pt} | None = None"
                (req_args if required else opt_args).append((arg(prop), decl))
            for q, required, qt in meth["query_params"]:
                decl = f"{arg(q)}: {qt}" if required else f"{arg(q)}: {qt} | None = None"
                (req_args if required else opt_args).append((arg(q), decl))

            req_args.sort(key=lambda x: x[0])
            opt_args.sort(key=lambda x: x[0])
            args = ["self"] + [decl for _, decl in req_args + opt_args]
            kwargs = [f"{name}={name}" for name, _ in req_args + opt_args]
            sig = ", ".join(args) if len(args) == 1 else "self, *, " + ", ".join(args[1:])
            call = f"{meth['cls']}({', '.join(kwargs)})"
            paged = meth["pagination"] is not None

            param_docs = _param_lines(meth, kwargs)

            if paged:
                # auto_paginate=True walks every page; one page by default.
                sig_c = sig + ", auto_paginate: bool = False"
                out.append(f"    async def {meth['name']}({sig_c}) -> {meth['return_type']} | list[Any]:")
                out.append(f'        """{safe_doc(meth["summary"])}')
                out.append("")
                out.extend(param_docs)
                out.append("        :param auto_paginate: автоматически собрать все страницы выборки")
                out.append('        """')
                out.append(f"        call = {call}")
                if meth["return_type"] == "None":
                    out.append("        if auto_paginate:")
                    out.append("            return await call.paginate(self._api)")
                    out.append("        await call.emit(self._api)")
                    out.append("        return None")
                else:
                    out.append(
                        "        return await call.paginate(self._api) if auto_paginate "
                        "else await call.emit(self._api)"
                    )
                out.append("")
                out.append(f"    async def iter_{meth['name']}({sig}) -> AsyncIterator[Any]:")
                if param_docs:
                    out.append(f'        """{safe_doc(meth["summary"])} — постранично, по одной записи.')
                    out.append("")
                    out.extend(param_docs)
                    out.append('        """')
                else:
                    out.append(f'        """{safe_doc(meth["summary"])} — постранично, по одной записи."""')
                out.append(f"        async for item in {call}.stream(self._api):")
                out.append("            yield item")
                out.append("")
            else:
                out.append(f"    async def {meth['name']}({sig}) -> {meth['return_type']}:")
                if param_docs:
                    out.append(f'        """{safe_doc(meth["summary"])}')
                    out.append("")
                    out.extend(param_docs)
                    out.append('        """')
                else:
                    out.append(f'        """{safe_doc(meth["summary"])}"""')
                if meth["return_type"] == "None":
                    out.append(f"        await {call}.emit(self._api)")
                else:
                    out.append(f"        return await {call}.emit(self._api)")
                out.append("")

        used = sorted({meth["cls"] for meth in self.methods})
        # An empty parenthesised import is a SyntaxError, so a section that
        # collected nothing must render no import at all.
        block = "from .methods import (\n" + "".join(f"    {c},\n" for c in used) + ")" if used else ""
        rendered = "\n".join(out).replace("@IMPORTS@", block)
        rendered = rendered.replace("@MODELS@", self._models_import(out))
        iter_import = (
            "from collections.abc import AsyncIterator\n"
            if "AsyncIterator" in rendered.split("@ITER@")[-1]
            else ""
        )
        rendered = rendered.replace("@ITER@\n", iter_import)
        typing_names = ["TYPE_CHECKING"]
        if re.search(r"\bAny\b", rendered.split("@TYPING2@")[-1]):
            typing_names.append("Any")
        return rendered.replace("@TYPING2@", f"from typing import {', '.join(typing_names)}")


# Spec file -> section package. 05-orders-dbs is skipped: its paths are a
# subset of 05-dbs, which is newer.
SECTIONS: dict[str, str] = {
    "01-general.yaml": "general",
    "02-items.yaml": "items",
    "03-orders-fbs.yaml": "orders_fbs",
    "04-orders-dbw.yaml": "orders_dbw",
    "05-dbs.yaml": "orders_dbs",
    "06-in-store-pickup.yaml": "in_store_pickup",
    "07-orders-fbw.yaml": "orders_fbw",
    "08-promotion.yaml": "promotion",
    "09-communications.yaml": "communications",
    "10-rates.yaml": "rates",
    "11-analytics.yaml": "analytics",
    "12-reports.yaml": "reports",
    "13-finances.yaml": "finances",
    "14-wbd.yaml": "wbd",
}

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS_DIR = ROOT / "specs"
PACKAGE = ROOT / "src" / "wbapi"


class SpecError(RuntimeError):
    """A spec that cannot be turned into a section."""


def load_spec(spec_file: pathlib.Path) -> dict:
    """Parse a spec and refuse the shapes that would generate nothing.

    Without these checks a spec that changed shape — or that arrived as an
    antibot HTML page — yields zero methods and silently overwrites a working
    section with an empty one.
    """
    try:
        spec = yaml.safe_load(spec_file.read_text())
    except yaml.YAMLError as exc:
        raise SpecError(f"not valid YAML: {exc}") from exc

    if not isinstance(spec, dict):
        raise SpecError(f"expected a mapping at the top level, got {type(spec).__name__}")
    paths = spec.get("paths")
    if not isinstance(paths, dict) or not paths:
        raise SpecError("no paths")
    return spec


def generate_section(spec_file: pathlib.Path, package: str) -> tuple[int, int, str]:
    generator = Generator(load_spec(spec_file), package)
    generator.collect()

    # Writing an empty section would drop every method the package already has.
    if not generator.methods:
        raise SpecError("no methods survived generation")

    out_dir = PACKAGE / package
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "models.py").write_text(generator.render_types())
    (out_dir / "methods.py").write_text(generator.render_methods())
    (out_dir / "__init__.py").write_text(generator.render_facade())

    structs = len([x for x in generator.structs.values() if x])
    return structs, len(generator.methods), generator.title


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if only and only not in SECTIONS.values():
        known = ", ".join(sorted(SECTIONS.values()))
        print(f"unknown section {only!r}; known: {known}", file=sys.stderr)
        return 2

    built: dict[str, str] = {}
    failed: list[str] = []
    total_methods = total_models = 0

    for spec_name, package in SECTIONS.items():
        if only and only != package:
            continue
        spec_file = SPECS_DIR / spec_name
        if not spec_file.exists():
            print(f"  ! {spec_name}: missing", file=sys.stderr)
            failed.append(package)
            continue
        try:
            models, methods, title = generate_section(spec_file, package)
        except SpecError as exc:
            # The section on disk is left alone: a bad spec must not erase it.
            print(f"  ! {spec_name}: {exc}", file=sys.stderr)
            failed.append(package)
            continue
        built[package] = pascal(package)
        total_models += models
        total_methods += methods
        print(f"  {package:18} {methods:4d} methods, {models:4d} models   {title}")

    files = [str(f) for package in SECTIONS.values() for f in (PACKAGE / package).rglob("*.py")]
    for args in (["check", "--select", "I,F401", "--fix", "-q"], ["format", "-q"]):
        result = subprocess.run(["ruff", *args, *files], capture_output=True, text=True)
        if result.returncode not in (0, 1):
            print(f"  ! ruff {args[0]}: {result.stderr.strip()}", file=sys.stderr)

    print(f"\ntotal: {total_methods} methods, {total_models} models in {len(built)} sections")
    if failed:
        print(f"failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
