# AGENTS.md

This file defines how coding agents should contribute to `wbapi`.

## Scope and defaults

- Base branch: `main`
- Distribution: `wbapi-async` on PyPI, imported as `wbapi`
- Python: `>=3.10,<3.14`
- Main tooling: `uv`, `ruff`, `mypy`, `pytest`
- Keep diffs focused; avoid unrelated refactors/reformatting.

API documentation: https://dev.wildberries.ru/en/docs/openapi/api-information
OpenAPI specs: https://dev.wildberries.ru/api/swagger/yaml/ru/ (`01-general.yaml` … `14-wbd.yaml`)

## Codebase Navigation

Use **Serena MCP** for all codebase navigation tasks. Serena provides semantic, symbol-aware tools that are more efficient than raw file reads:

- `get_symbols_overview` — list classes/methods in a file without reading the full body
- `find_symbol` — locate a specific class, method, or field by name path
- `find_referencing_symbols` — find all usages of a symbol across the codebase
- `search_for_pattern` — regex search when symbol names are unknown

Prefer Serena's symbol tools over `Read`/`Grep` for source code exploration. Only fall back to file-based tools when Serena is unavailable or for non-code files (JSON configs, Markdown, etc.).

## Module map

Hand-written:

| File                | Role                                                      |
| ------------------- | --------------------------------------------------------- |
| `client/api.py`     | `WBApi` — holds the session and the section facades       |
| `client/session.py` | httpx transport, retries, rate limiting, error mapping    |
| `client/method.py`  | `WBMethod` — `emit`/`stream`/`paginate` and the six walks |
| `client/model.py`   | `WBModel` — `to_dict`/`to_json`/`from_dict` over msgspec  |
| `exceptions.py`     | `WBError` hierarchy                                       |
| `utils/token.py`    | JWT decoding: category, scopes, expiry                    |
| `__init__.py`       | `WBApi`, `__version__`, and the `SECTIONS` registry       |

Generated, one package per section, listed in `SECTIONS`:

| File                    | Role                                          |
| ----------------------- | --------------------------------------------- |
| `<section>/methods.py`  | one `WBMethod` subclass per endpoint          |
| `<section>/models.py`   | the `WBModel` structs those methods return    |
| `<section>/__init__.py` | the facade `WBApi` exposes as `api.<section>` |

The section packages sit beside the hand-written ones, so a directory listing
no longer tells them apart — `SECTIONS` is what does.

## Invariants

Break these and something fails in production, not in CI:

- **The token is a client-level header**, set once in `Session.__init__`. Never
  assign it per request — concurrent calls would race and leak the token to
  public hosts.
- **Rate limits ride on the method class.** Each `WBMethod` carries its own
  `__rate_limits__` read from the spec, keyed by token category. Never look a
  limit up by URL — a concrete path would inherit its parent's quota.
- **Limiters are keyed weakly by event loop.** An `AsyncLimiter` bound to a dead
  loop misbehaves; never make the cache a plain global dict.
- **Error payloads are not always dicts.** WB returns RFC 7807 objects, bare
  lists, and plain text. Never index or splat a payload without checking.
- **Every pagination strategy must terminate** — bounded by `MAX_PAGES` and by
  detecting a repeated cursor.
- **Responses are `WBModel` structs**, not dicts. Use `to_dict()` for a plain
  mapping and `to_dict(by_alias=True)` for the original Wildberries field names.
- **Every pagination walk lives on `WBMethod`.** Six of them (`_walk_next`,
  `_walk_cursor`, `_walk_rrdid`, `_walk_skip_take`, `_walk_offset_query`,
  `_walk_offset_body`); the spec decides which one a method gets.

## Regenerating the client

The section packages are generated from the specs in `specs/`. Never edit them
by hand — change the generator instead:

```console
uv run python scripts/update_specs.py        # refresh specs/ from Wildberries
uv run python scripts/codegen.py           # regenerate every section
uv run python scripts/codegen.py items     # regenerate one section
```

`update_specs.py` drives a headless browser, because dev.wildberries.ru answers
plain requests with HTTP 498. It refuses to overwrite when nothing could be
fetched.

`codegen.py` names a method after the leading verb of its summary rather than
the HTTP verb — Wildberries often uses POST for reads — and reads rate limits
out of the markdown tables in each endpoint's description. Two tables hold the
cases the specs get wrong: `SPEC_FIXES` for schemas that disagree with the live
response, `NAME_FIXES` for paths that carry less meaning than the endpoint.

`scripts/smoke_check.py` runs read-only calls against the live API; it needs
`WB_TOKEN` in the environment.

## Adding a pagination scheme

- Add the walk as a `_walk_*` method on `WBMethod` in `client/method.py`
- Teach `detect_pagination` in `scripts/codegen.py` to recognise its shape,
  ordered so a more specific one wins
- Bound the loop by `MAX_PAGES` and stop on a repeated cursor
- Cover it in `tests/test_pagination.py` with a handler that serves two pages

## Checks

```console
uv run pytest --cov
uv run mypy
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
```

All four must pass before a change is complete.
