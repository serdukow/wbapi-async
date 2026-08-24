from importlib.metadata import PackageNotFoundError, version

from .client import WBApi


# The generated section packages. Kept here because they now sit beside the
# hand-written ones, so a directory listing no longer tells them apart.
SECTIONS = (
    "analytics",
    "communications",
    "finances",
    "general",
    "in_store_pickup",
    "items",
    "orders_dbs",
    "orders_dbw",
    "orders_fbs",
    "orders_fbw",
    "promotion",
    "rates",
    "reports",
    "wbd",
)


try:
    __version__ = version("wbapi-async")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__all__ = ("SECTIONS", "WBApi", "__version__")
