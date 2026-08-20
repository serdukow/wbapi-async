#!/usr/bin/env python3
"""Regenerate ``src/wbapi/endpoints.py`` from the Wildberries OpenAPI specs.

Fetches every published spec, extracts each path together with the server it
lives on and its declared rate limit, and rewrites the generated block of
``endpoints.py`` in place. Paths already present but missing from the current
specs are kept and marked deprecated, so a spec regression cannot break code
that still works against the live API.

Usage::

    python scripts/generate_endpoints.py            # rewrite endpoints.py
    python scripts/generate_endpoints.py --check    # exit 1 if out of date
"""

from __future__ import annotations

import argparse
import asyncio
from collections import defaultdict
from pathlib import Path
import re
import sys
from typing import Any, NamedTuple

import httpx
import yaml


SPEC_BASE = "https://dev.wildberries.ru/api/swagger/yaml/en"
SPEC_FILES = (
    "01-general.yaml",
    "02-content.yaml",
    "03-prices.yaml",
    "04-marketplace.yaml",
    "05-statistics.yaml",
    "06-analytics.yaml",
    "07-promotion.yaml",
    "08-feedbacks.yaml",
    "09-buyers-chat.yaml",
    "10-supplies.yaml",
    "11-returns.yaml",
    "12-documents.yaml",
    "13-finances.yaml",
)

TARGET = Path(__file__).resolve().parent.parent / "src" / "wbapi" / "endpoints.py"

BEGIN = "# --- BEGIN GENERATED ---"
END = "# --- END GENERATED ---"

# x-rate-limit extensions WB uses, in the order we prefer them.
_BURST_KEYS = ("x-rate-limit-burst", "x-burst", "burst")
_INTERVAL_KEYS = ("x-rate-limit-interval", "x-interval", "interval")

DEFAULT_INTERVAL_MS = 1000
DEFAULT_BURST = 5


class Endpoint(NamedTuple):
    path: str
    host: str
    interval_ms: int
    burst: int


async def _fetch(client: httpx.AsyncClient, name: str) -> dict[str, Any] | None:
    url = f"{SPEC_BASE}/{name}"
    try:
        response = await client.get(url)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        print(f"  ! {name}: {exc}", file=sys.stderr)
        return None
    data = yaml.safe_load(response.text)
    return data if isinstance(data, dict) else None


def _servers(spec: dict[str, Any]) -> list[str]:
    hosts = []
    for server in spec.get("servers") or []:
        url = server.get("url") if isinstance(server, dict) else None
        if isinstance(url, str) and url.startswith("https://"):
            hosts.append(url.rstrip("/"))
    return hosts


def _rate_limit(operations: dict[str, Any]) -> tuple[int, int]:
    """Read burst/interval hints from any operation on a path."""
    interval, burst = DEFAULT_INTERVAL_MS, DEFAULT_BURST
    for operation in operations.values():
        if not isinstance(operation, dict):
            continue
        for key in _BURST_KEYS:
            value = operation.get(key)
            if isinstance(value, int) and value > 0:
                burst = value
                break
        for key in _INTERVAL_KEYS:
            value = operation.get(key)
            if isinstance(value, int) and value > 0:
                interval = value
                break
    return interval, burst


def _collect(specs: list[dict[str, Any]]) -> dict[str, Endpoint]:
    found: dict[str, Endpoint] = {}
    for spec in specs:
        hosts = _servers(spec)
        if not hosts:
            continue
        host = hosts[0]
        for path, operations in (spec.get("paths") or {}).items():
            if not isinstance(path, str) or not path.startswith("/"):
                continue
            if not isinstance(operations, dict):
                continue
            interval, burst = _rate_limit(operations)
            found[path] = Endpoint(path, host, interval, burst)
    return found


def _parse_existing(text: str) -> dict[str, Endpoint]:
    """Read the current table so removals can be preserved."""
    existing: dict[str, Endpoint] = {}
    host: str | None = None
    for line in text.splitlines():
        host_match = re.match(r'\s*"(https://[^"]+)":\s*\{', line)
        if host_match:
            host = host_match.group(1)
            continue
        entry = re.match(r'\s*"(/[^"]*)":\s*\((\d+),\s*(\d+)\)', line)
        if entry and host:
            existing[entry.group(1)] = Endpoint(
                entry.group(1), host, int(entry.group(2)), int(entry.group(3))
            )
    return existing


def _render(endpoints: dict[str, Endpoint], deprecated: set[str]) -> str:
    by_host: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints.values():
        by_host[endpoint.host].append(endpoint)

    lines = [BEGIN, "", "ENDPOINTS: dict[str, dict[str, tuple[int, int]]] = {"]
    for host in sorted(by_host, key=lambda h: (-len(by_host[h]), h)):
        lines.append(f'    "{host}": {{')
        for endpoint in sorted(by_host[host], key=lambda e: e.path):
            suffix = "  # deprecated" if endpoint.path in deprecated else ""
            lines.append(f'        "{endpoint.path}": ({endpoint.interval_ms}, {endpoint.burst}),{suffix}')
        lines.append("    },")
    lines.extend(["}", "", END])
    return "\n".join(lines)


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 when out of date")
    args = parser.parse_args()

    print(f"Fetching {len(SPEC_FILES)} specs from {SPEC_BASE} …")
    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        results = await asyncio.gather(*(_fetch(client, name) for name in SPEC_FILES))
    specs = [spec for spec in results if spec is not None]

    if not specs:
        print("No specs could be fetched; refusing to rewrite the table.", file=sys.stderr)
        return 2

    found = _collect(specs)
    print(f"  parsed {len(specs)}/{len(SPEC_FILES)} specs, {len(found)} paths")

    current_text = TARGET.read_text() if TARGET.exists() else ""
    existing = _parse_existing(current_text)

    # Preserve paths that vanished from the spec but may still work.
    deprecated = set(existing) - set(found)
    merged = {**{path: existing[path] for path in deprecated}, **found}

    added = sorted(set(found) - set(existing))
    if added:
        print(f"  + {len(added)} new: " + ", ".join(added[:5]) + (" …" if len(added) > 5 else ""))
    if deprecated:
        print(f"  ~ {len(deprecated)} no longer in spec (kept, marked deprecated)")

    block = _render(merged, deprecated)
    if BEGIN not in current_text or END not in current_text:
        print(f"{TARGET} is missing the generated markers.", file=sys.stderr)
        return 2

    start = current_text.index(BEGIN)
    stop = current_text.index(END) + len(END)
    updated = current_text[:start] + block + current_text[stop:]

    if updated == current_text:
        print("Already up to date.")
        return 0

    if args.check:
        print("endpoints.py is out of date; run scripts/generate_endpoints.py", file=sys.stderr)
        return 1

    TARGET.write_text(updated)
    print(f"Wrote {TARGET} ({len(merged)} endpoints).")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
