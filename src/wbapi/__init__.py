"""Async client for the Wildberries Seller API.

    from wbapi import WBApi

    async with WBApi(token="...") as api:
        orders = await api.get("/api/v3/orders/new", params={"limit": 10})

        async for supply in api.paginate("/api/v3/supplies"):
            print(supply.id)

Exceptions live in :mod:`wbapi.exceptions`::

    from wbapi.exceptions import WBError, WBRateLimitError
"""

from importlib.metadata import PackageNotFoundError, version

from .client import WBApi
from .pagination import Paginator
from .types import WBDict, WBList, WBObject


try:
    __version__ = version("wbapi-async")
except PackageNotFoundError:  # running from a source checkout
    __version__ = "0.0.0.dev0"

__all__ = (
    "WBApi",
    "WBObject",
    "WBDict",
    "WBList",
    "Paginator",
    "__version__",
)
