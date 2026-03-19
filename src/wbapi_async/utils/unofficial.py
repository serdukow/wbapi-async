from collections.abc import Callable
from functools import wraps
from typing import Any
import warnings


def unofficial(func: Callable[..., Any]) -> Callable[..., Any]:
    """Mark a method as unofficial (not documented in WB API docs)."""

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            f"{func.__name__} is an unofficial method and may stop working at any time.",
            stacklevel=2,
        )
        return await func(*args, **kwargs)

    wrapper.__unofficial__ = True  # type: ignore[attr-defined]
    wrapper.__doc__ = (
        f".. warning:: Unofficial method — not documented in WB API.\n\n{func.__doc__ or ''}"
    )
    return wrapper
