#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import html
from pathlib import Path
import re
import subprocess
import sys
import time

import yaml


ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = ROOT / "specs"

BASE_URL = "https://dev.wildberries.ru/api/swagger/yaml/ru"
SPEC_FILES = (
    "01-general.yaml",
    "02-items.yaml",
    "03-orders-fbs.yaml",
    "04-orders-dbw.yaml",
    "05-dbs.yaml",
    "06-in-store-pickup.yaml",
    "07-orders-fbw.yaml",
    "08-promotion.yaml",
    "09-communications.yaml",
    "10-rates.yaml",
    "11-analytics.yaml",
    "12-reports.yaml",
    "13-finances.yaml",
    "14-wbd.yaml",
)

CHALLENGE_MARKER = "__wbaas"
PAGE_TIMEOUT_MS = 60_000
CHALLENGE_WAITS_MS = (6_000, 8_000, 10_000)

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

# Wildberries serves an anti-bot challenge to anything that looks automated,
# so the page must not expose webdriver traits.
STEALTH = """
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
Object.defineProperty(navigator, 'languages', {get: () => ['ru-RU', 'ru', 'en-US']});
window.chrome = {runtime: {}};
"""

_PRE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.DOTALL)


def extract_yaml(body: str) -> str | None:
    match = _PRE.search(body)
    if match is None:
        return None
    text = html.unescape(match.group(1))
    try:
        parsed = yaml.safe_load(text)
    except yaml.YAMLError:
        return None
    return text if isinstance(parsed, dict) and parsed.get("paths") else None


async def download(names: tuple[str, ...]) -> dict[str, str]:
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print(
            "playwright is required: uv run --with playwright python scripts/update_specs.py",
            file=sys.stderr,
        )
        raise SystemExit(2) from None

    downloaded: dict[str, str] = {}
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            channel="chrome",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-first-run",
                "--no-default-browser-check",
            ],
        )
        context = await browser.new_context(
            locale="ru-RU",
            viewport={"width": 1280, "height": 800},
            user_agent=USER_AGENT,
        )
        await context.add_init_script(STEALTH)
        page = await context.new_page()

        async def load(name: str) -> str | None:
            await page.goto(
                f"{BASE_URL}/{name}",
                wait_until="domcontentloaded",
                timeout=PAGE_TIMEOUT_MS,
            )
            body = await page.content()
            for wait in CHALLENGE_WAITS_MS:
                if CHALLENGE_MARKER not in body:
                    break
                await page.wait_for_timeout(wait)
                body = await page.content()
            return extract_yaml(body)

        try:
            for name in names:
                text = await load(name)
                if text is None:
                    await page.wait_for_timeout(5_000)
                    text = await load(name)
                if text is None:
                    print(f"  ! {name}: blocked or invalid", file=sys.stderr)
                    continue
                downloaded[name] = text
                print(f"  ok {name} ({len(text) // 1024} KB)")
        finally:
            await browser.close()

    return downloaded


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def new_endpoints() -> list[str]:
    diff = git("diff", "--", "src/wbapi/resources")
    return [
        line.split('"')[1]
        for line in diff.splitlines()
        if line.startswith("+") and "__path__" in line and '"' in line
    ]


def open_pull_request(added: list[str]) -> int:
    branch = f"chore/update-specs-{time.strftime('%Y%m%d')}"
    title = "feat: update the client from the Wildberries specs"
    body = "Specs refreshed, client regenerated, tests passed."
    if added:
        listed = "\n".join(f"- `{path}`" for path in added[:20])
        more = f"\n\n…and {len(added) - 20} more" if len(added) > 20 else ""
        body = f"New endpoints:\n{listed}{more}\n\n{body}"

    git("checkout", "-B", branch)
    git("add", "specs", "src/wbapi/resources")
    git("commit", "-m", title)
    git("push", "-u", "origin", branch, "--force-with-lease")

    result = subprocess.run(
        ["gh", "pr", "create", "--title", title, "--body", body, "--base", "main"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    print(result.stdout.strip() or result.stderr.strip())
    return result.returncode


def regenerate() -> bool:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "codegen.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
    return result.returncode == 0


async def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download the Wildberries OpenAPI specs and regenerate the client."
    )
    parser.add_argument("--check", action="store_true", help="exit 1 if specs changed")
    parser.add_argument("--pr", action="store_true", help="run tests and open a pull request")
    args = parser.parse_args()

    SPECS_DIR.mkdir(exist_ok=True)
    print(f"Downloading {len(SPEC_FILES)} specs …")
    downloaded = await download(SPEC_FILES)

    if not downloaded:
        print("Nothing could be downloaded; specs left untouched.", file=sys.stderr)
        return 2

    changed = [
        name
        for name, text in downloaded.items()
        if not (SPECS_DIR / name).exists() or (SPECS_DIR / name).read_text() != text
    ]

    print(f"\n{len(downloaded)}/{len(SPEC_FILES)} downloaded, {len(changed)} changed")
    if not changed:
        print("Specs are up to date.")
        return 0

    if args.check:
        print(f"Out of date: {', '.join(changed)}", file=sys.stderr)
        return 1

    for name in changed:
        (SPECS_DIR / name).write_text(downloaded[name])
    print(f"Updated: {', '.join(changed)}\n")

    if not regenerate():
        return 1

    if not args.pr:
        print("\nReview the diff, then commit or rerun with --pr.")
        return 0

    if subprocess.run(["uv", "run", "pytest", "-q"], cwd=ROOT).returncode != 0:
        print("Tests failed; no pull request opened.", file=sys.stderr)
        return 1

    return open_pull_request(new_endpoints())


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
