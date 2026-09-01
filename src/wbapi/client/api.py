from __future__ import annotations

from types import TracebackType
from typing import Any

import httpx

from ..analytics import Analytics
from ..communications import Communications
from ..exceptions import WBAuthError, WBConfigurationError
from ..finances import Finances
from ..general import General
from ..in_store_pickup import InStorePickup
from ..items import Items
from ..orders_dbs import OrdersDbs
from ..orders_dbw import OrdersDbw
from ..orders_fbs import OrdersFbs
from ..orders_fbw import OrdersFbw
from ..promotion import Promotion
from ..rates import Rates
from ..reports import Reports
from ..utils.token import decode_token
from ..wbd import Wbd
from .method import WBMethod
from .session import DEFAULT_TIMEOUT, Session


__all__ = ("WBApi",)


class WBApi:
    """Клиент для работы с WB API.

    Args:
        token: Токен авторизации продавца.
        timeout: Таймаут запроса в секундах.
        sandbox: Вы можете протестировать методы API на случайных данных.
                 Для этого понадобится токен с опцией Тестовый контур.
                 Данные в тестовом контуре сгенерированы случайным образом
                 и не принадлежат реальным продавцам.
                Использование тестового контура не несёт риска непреднамеренного раскрытия информации.

    Raises:
        WBConfigurationError.
    """

    __slots__ = (
        "_session",
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
        "sandbox",
        "token",
        "wbd",
    )

    def __init__(
        self,
        token: str,
        *,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        sandbox: bool = False,
        **kwargs: Any,
    ) -> None:
        if not isinstance(token, str) or not token.strip():
            raise WBConfigurationError(
                "Некорректный токен авторизации. "
                "См. https://dev.wildberries.ru/docs/openapi/api-information#tag/authorization/Kategorii-tokenov"
            )
        self.token = decode_token(token.strip())
        self.sandbox = sandbox
        self._session = Session(token.strip(), timeout=timeout, **kwargs)
        self.analytics = Analytics(self)
        self.communications = Communications(self)
        self.finances = Finances(self)
        self.general = General(self)
        self.in_store_pickup = InStorePickup(self)
        self.items = Items(self)
        self.orders_dbs = OrdersDbs(self)
        self.orders_dbw = OrdersDbw(self)
        self.orders_fbs = OrdersFbs(self)
        self.orders_fbw = OrdersFbw(self)
        self.promotion = Promotion(self)
        self.rates = Rates(self)
        self.reports = Reports(self)
        self.wbd = Wbd(self)

    def __repr__(self) -> str:
        return f"WBApi(token={self._session.masked_token})"

    async def _send(
        self,
        method: WBMethod[Any],
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
    ) -> Any:
        scope = getattr(method, "__scope__", None)
        if scope is not None and not self.token.allows(scope):
            raise WBAuthError(
                "Проверьте токен авторизации: Категория токена должна совпадать с категорией API. "
                "См. https://dev.wildberries.ru/docs/openapi/api-information#tag/authorization/Dekodirovanie-tokena",
                status_code=403,
            )

        kind = self.token.kind.name.lower() if self.token.kind else None
        return await self._session.request(
            method.__http_method__,
            method.url(self.sandbox),
            limit_key=method.__path__,
            rate_limit=method.rate_limit(kind),
            params=params,
            json=json,
        )

    async def close(self) -> None:
        await self._session.close()

    async def __aenter__(self) -> WBApi:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.close()
