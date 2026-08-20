# AGENTS.md

This file defines how coding agents should contribute to `wbapi`.

## Scope and defaults

- Base branch: `main`
- Distribution: `wbapi-async` on PyPI, imported as `wbapi`
- Python: `>=3.10,<3.14`
- Main tooling: `uv`, `ruff`, `mypy`, `pytest`
- Keep diffs focused; avoid unrelated refactors/reformatting.

API documentation: https://dev.wildberries.ru/en/docs/openapi/api-information
OpenAPI specs: https://dev.wildberries.ru/api/swagger/yaml/en/ (`01-general.yaml` … `13-finances.yaml`)

## Codebase Navigation

Use **Serena MCP** for all codebase navigation tasks. Serena provides semantic, symbol-aware tools that are more efficient than raw file reads:

- `get_symbols_overview` — list classes/methods in a file without reading the full body
- `find_symbol` — locate a specific class, method, or field by name path
- `find_referencing_symbols` — find all usages of a symbol across the codebase
- `search_for_pattern` — regex search when symbol names are unknown

Prefer Serena's symbol tools over `Read`/`Grep` for source code exploration. Only fall back to file-based tools when Serena is unavailable or for non-code files (JSON configs, Markdown, etc.).

## Module map

| File            | Role                                                                  |
| --------------- | --------------------------------------------------------------------- |
| `client.py`     | `WBApi` — get/post/put/patch/delete/paginate                           |
| `session.py`    | httpx transport, retries, rate limiting, error mapping                 |
| `pagination.py` | `Paginator` — async iterator plus the per-scheme strategies            |
| `endpoints.py`  | endpoint table and URL resolution                                      |
| `exceptions.py` | `WBError` hierarchy                                                    |
| `types.py`      | `WBDict` / `WBList` — dict and list subclasses with attribute access    |

## Invariants

Break these and something fails in production, not in CI:

- **The token is a client-level header**, set once in `Session.__init__`. Never
  assign it per request — concurrent calls would race and leak the token to
  public hosts.
- **Rate limits are looked up by path template.** A concrete path like
  `/api/v3/orders/123/cancel` must go through `_match_template` so it keeps its
  own quota instead of inheriting its parent's.
- **Limiters are keyed weakly by event loop.** An `AsyncLimiter` bound to a dead
  loop misbehaves; never make the cache a plain global dict.
- **Error payloads are not always dicts.** WB returns RFC 7807 objects, bare
  lists, and plain text. Never index or splat a payload without checking.
- **Every pagination strategy must terminate** — bounded by `MAX_PAGES` and by
  detecting a repeated cursor.
- **Responses subclass `dict`/`list`**, so `json.dumps` and `{**record}` work
  without conversion. `WBObject` is only a marker base — too empty to use as a
  return type.

## Editing the endpoint table

`endpoints.py` holds a generated block between `# --- BEGIN GENERATED ---` and
`# --- END GENERATED ---`. Do not hand-edit it; regenerate instead:

```console
uv run python scripts/generate_endpoints.py           # rewrite
uv run python scripts/generate_endpoints.py --check   # CI freshness check
```

The generator refuses to write when no spec could be fetched, and keeps paths
that vanished from the spec (marked deprecated) so live endpoints keep working.
A weekly workflow opens a PR when the table changes.

Everything outside the generated block — `PUBLIC_HOSTS`, `PAGE_SIZES`, the
lookup functions — is safe to edit by hand.

## Adding a pagination scheme

- Add the strategy as a `_by_*` method on `Paginator`
- Register it in `_detect`, ordered so a more specific shape wins
- Bound the loop and stop on a repeated cursor
- Cover it in `tests/test_pagination.py` with a handler that serves two pages

## Checks

```console
uv run pytest --cov
uv run mypy
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
```

All four must pass before a change is complete.
