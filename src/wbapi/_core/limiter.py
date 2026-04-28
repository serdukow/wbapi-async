from aiolimiter import AsyncLimiter

from ._registry import _LIMITS


_DEFAULT_LIMIT: tuple[int, int, int, int] = (60000, 60, 1000, 5)

_limiters: dict[tuple[int, int], AsyncLimiter] = {}


def _get_limiter(path: str) -> AsyncLimiter:
    period, limit, interval, burst = _LIMITS.get(path, _DEFAULT_LIMIT)
    key = (interval, burst)
    if key not in _limiters:
        _limiters[key] = AsyncLimiter(max_rate=burst, time_period=interval / 1000)
    return _limiters[key]
