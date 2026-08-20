#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass
import importlib
from pathlib import Path
import pkgutil
import re
import sys
import time
from typing import Any


sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from wbapi import WBApi
from wbapi.client.method import WBMethod
from wbapi.exceptions import WBAPIError, WBConfigurationError, WBDecodeError, WBError
from wbapi.utils import Scope


@dataclass(frozen=True)
class Check:
    section: str
    method: str
    scope: Scope | None
    sandbox: bool


@dataclass
class Result:
    check: Check
    status: str
    detail: str = ""
    elapsed_ms: float = 0.0


def discover(sandbox_only: bool) -> list[Check]:
    import wbapi.resources as resources

    checks: list[Check] = []
    for module in pkgutil.iter_modules(resources.__path__):
        methods = importlib.import_module(f"wbapi.resources.{module.name}.methods")
        for name in dir(methods):
            cls = getattr(methods, name)
            if not isinstance(cls, type) or not issubclass(cls, WBMethod):
                continue
            if getattr(cls, "__http_method__", "") != "GET":
                continue
            if getattr(cls, "__struct_fields__", ()):
                continue
            if sandbox_only and not getattr(cls, "__sandbox_host__", ""):
                continue
            checks.append(
                Check(
                    section=module.name,
                    method=re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower(),
                    scope=getattr(cls, "__scope__", None),
                    sandbox=bool(getattr(cls, "__sandbox_host__", "")),
                )
            )
    return sorted(checks, key=lambda c: (c.section, c.method))


def summarize(value: Any, limit: int = 72) -> str:
    if value is None:
        return "empty"
    if isinstance(value, list):
        return f"{len(value)} items"
    fields = getattr(value, "__struct_fields__", None)
    if not fields:
        return type(value).__name__
    parts = []
    for name in fields:
        item = getattr(value, name, None)
        if item is None:
            continue
        if isinstance(item, list):
            parts.append(f"{name}={len(item)} items")
        elif hasattr(item, "__struct_fields__"):
            parts.append(f"{name}={type(item).__name__}")
        else:
            parts.append(f"{name}={item!r}")
        if len(", ".join(parts)) > limit:
            break
    if not parts:
        return "empty"
    body = ", ".join(parts)
    return body[:limit] + "…" if len(body) > limit else body


async def run_check(api: WBApi, check: Check) -> Result:
    if check.scope is not None and not api.token.allows(check.scope):
        return Result(check, "skip", f"token lacks {check.scope.name}")

    started = time.perf_counter()
    try:
        value = await getattr(getattr(api, check.section), check.method)()
    except WBConfigurationError as exc:
        return Result(check, "skip", str(exc))
    except WBDecodeError as exc:
        return Result(check, "fail", f"response does not match the spec: {exc}")
    except WBAPIError as exc:
        if exc.status_code in (401, 403):
            return Result(check, "skip", f"HTTP {exc.status_code}")
        return Result(check, "fail", f"HTTP {exc.status_code}: {exc}")
    except WBError as exc:
        return Result(check, "fail", f"{type(exc).__name__}: {exc}")

    elapsed = (time.perf_counter() - started) * 1000
    return Result(check, "ok", summarize(value), elapsed)


async def main() -> int:
    parser = argparse.ArgumentParser(description="Call read-only endpoints against the live Wildberries API.")
    parser.add_argument(
        "--sandbox",
        action="store_true",
        help="use the test contour (requires a test-contour token)",
    )
    parser.add_argument("--verbose", action="store_true", help="print every check")
    args = parser.parse_args()

    token = __import__("os").environ.get("WB_TOKEN", "").strip()
    if not token:
        print("WB_TOKEN is not set", file=sys.stderr)
        return 2

    sandbox = args.sandbox
    checks = discover(sandbox_only=sandbox)
    if not checks:
        print("nothing to check", file=sys.stderr)
        return 2

    contour = "sandbox" if sandbox else "production"
    print(f"{contour}: {len(checks)} read-only endpoints")

    results: list[Result] = []
    try:
        api = WBApi(token=token, max_retries=1, sandbox=sandbox)
    except WBConfigurationError as exc:
        print(exc, file=sys.stderr)
        return 2

    async with api:
        for check in checks:
            result = await run_check(api, check)
            results.append(result)
            if args.verbose or result.status == "fail":
                mark = {"ok": "ok  ", "skip": "skip", "fail": "FAIL"}[result.status]
                label = f"{check.section}.{check.method}"
                timing = f"{result.elapsed_ms:5.0f}ms" if result.status == "ok" else "       "
                print(f"  {mark} {label:52} {timing} {result.detail}")

    passed = sum(r.status == "ok" for r in results)
    skipped = sum(r.status == "skip" for r in results)
    failed = [r for r in results if r.status == "fail"]

    print()
    if failed:
        print(f"{len(failed)} failed, {passed} passed, {skipped} skipped\n")
        for result in failed:
            print(f"  {result.check.section}.{result.check.method}")
            print(f"    {result.detail}")
        return 1

    print(f"All checks passed ({passed} passed, {skipped} skipped)")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
