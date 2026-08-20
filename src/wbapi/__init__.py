from importlib.metadata import PackageNotFoundError, version

from .client import WBApi


try:
    __version__ = version("wbapi-async")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__all__ = ("WBApi", "__version__")
