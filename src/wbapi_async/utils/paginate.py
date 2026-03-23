"""paginate() — fetch all pages from a paginated API method.

Example::

    from wbapi_async import WbAPI, paginate

    async with WbAPI(token="...") as api:
        products = await paginate(
            api.get_products_with_prices, nm_id=123
        )
        orders = await paginate(
            api.get_assembly_orders, date_from=1700000000
        )
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import TypeAdapter


if TYPE_CHECKING:
    from ..client.api import WbAPI


async def paginate(method: Any, **kwargs: Any) -> list[Any]:
    """Fetch all pages from a paginated API method and return a combined list.

    Args:
        method: A bound method from WbAPI (e.g. ``api.get_products_with_prices``).
        **kwargs: Parameters to pass to the method (excluding pagination params).

    Returns:
        Combined list of all items from all pages.

    Raises:
        TypeError: If the method does not support pagination.

    Example::

        products = await paginate(
            api.get_products_with_prices, nm_id=123
        )
    """
    from ..methods.pagination import PAGINATION_STRATEGIES  # lazy — avoids circular import

    # Resolve WbAPI instance and WbMethod class from the bound method
    wb_api: WbAPI = method.__self__
    method_cls = getattr(method, "__wrapped_cls__", None)
    if method_cls is None:
        raise TypeError(
            f"{method.__name__!r} does not expose __wrapped_cls__. "
            "Only auto-generated WbAPI methods support paginate()."
        )

    pagination_key: str | None = method_cls.__dict__.get("__pagination__")
    if not isinstance(pagination_key, str):
        raise TypeError(f"{method_cls.__name__} does not support pagination (__pagination__ is not set)")

    strategy = PAGINATION_STRATEGIES[pagination_key]
    pagination_params = strategy.first_params()

    # Use model_construct to skip validation — pagination params are injected separately
    instance = method_cls.model_construct(**kwargs)
    return_type = method_cls.__return__
    adapter: TypeAdapter[Any] = TypeAdapter(list[return_type])  # type: ignore[valid-type]

    wb_api.session.headers.set_token(wb_api._token)
    url = instance._get_url(wb_api)
    request_limit = getattr(instance, "request_limit", None)
    http_method = getattr(instance, "__http_method__", "GET").upper()
    base_params = instance.model_dump(by_alias=True, exclude_none=True, exclude={"request_limit"})
    result: list[Any] = []

    while True:
        raw = await instance._dispatch(
            wb_api, http_method, url, {**base_params, **pagination_params}, request_limit
        )
        page_raw = instance._extract(raw)
        if not page_raw:
            return result
        result.extend(adapter.validate_python(page_raw))
        pagination_params = strategy.next_params(pagination_params, raw, page_raw)
        if pagination_params is None:
            return result
