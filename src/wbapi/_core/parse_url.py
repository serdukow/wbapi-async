from ._registry import _BASES, _PUBLIC


def parse_url(path: str) -> str:
    """Resolve full URL for a spec path like /api/v3/supplies.

    If a full URL is passed, it is returned as-is provided its host is a known
    wildberries.ru domain or is listed in ``_PUBLIC``.
    """
    from urllib.parse import urlparse

    from ..exceptions import WBAPIError

    if path.startswith("https://") or path.startswith("http://"):
        host = urlparse(path).netloc
        known_hosts = {urlparse(v).netloc for v in _BASES.values()} | _PUBLIC
        if host not in known_hosts:
            raise WBAPIError(detail=f"Unknown host {host!r}.")
        return path

    base = _BASES.get(path)
    if base:
        return base + path
    parts = path.rstrip("/").split("/")
    for i in range(len(parts) - 1, 0, -1):
        candidate = "/".join(parts[:i])
        if candidate in _BASES:
            return _BASES[candidate] + path
    raise WBAPIError(
        detail=f"{path!r} may be deprecated or removed. See https://dev.wildberries.ru/release-notes"
    )
