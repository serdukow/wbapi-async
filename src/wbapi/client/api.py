from __future__ import annotations

from types import TracebackType
from typing import Any

import httpx

from ..exceptions import WBAuthError, WBConfigurationError
from ..resources import (
    Analytics,
    Communications,
    Finances,
    General,
    InStorePickup,
    Items,
    OrdersDbs,
    OrdersDbw,
    OrdersFbs,
    OrdersFbw,
    Promotion,
    Rates,
    Reports,
    Wbd,
)
from ..utils.token import TokenKind, decode_token
from .method import WBMethod
from .session import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_RETRY_WAIT,
    DEFAULT_RETRY_BACKOFF,
    DEFAULT_TIMEOUT,
    Session,
)


__all__ = ("WBApi",)


class WBApi:
    """Асинхронный клиент для работы с Wildberries API.

    Методы сгруппированы по разделам документации::

        async with WBApi(token="abcToken") as api:
            orders = await api.fbs.orders_new()
            print(orders.orders[0].id)

            async for order in api.fbs.iter_orders(
                limit=1000, next_=0
            ):
                await save(order)

    Args:
        token: Токен авторизации продавца.
               Категория токена должна совпадать с сервисом,
               к которому идёт запрос.
        timeout: Таймаут запроса в секундах или ``httpx.Timeout``.
        max_retries: Число повторов при 429, 5xx и обрывах связи.
        retry_backoff: Базовая задержка экспоненциального роста, в секундах.
        max_retry_wait: Верхняя граница одной паузы между повторами.
        user_agent: Значение вместо ``wbapi/<версия>``.
        transport: Транспорт httpx.
        sandbox: Отправлять запросы в тестовый контур. Нужен токен с опцией
            «Тестовый контур».

    Raises:
        WBConfigurationError: Токен авторизации не задан.
    """

    __slots__ = (
        "_session",
        "sandbox",
        "token",
        "general",
        "items",
        "orders_fbs",
        "orders_dbw",
        "orders_dbs",
        "in_store_pickup",
        "orders_fbw",
        "promotion",
        "communications",
        "rates",
        "analytics",
        "reports",
        "finances",
        "wbd",
    )

    def __init__(
        self,
        token: str,
        *,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_backoff: float = DEFAULT_RETRY_BACKOFF,
        max_retry_wait: float = DEFAULT_MAX_RETRY_WAIT,
        user_agent: str | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        sandbox: bool = False,
    ) -> None:
        if not isinstance(token, str) or not token.strip():
            raise WBConfigurationError(
                "Не задан токен авторизации. "
                "См. https://dev.wildberries.ru/openapi/api-information#tag/authorization"
            )

        self.token = decode_token(token.strip())
        is_test_token = self.token.kind is TokenKind.TEST
        if sandbox and self.token.kind is not None and not is_test_token:
            raise WBConfigurationError(
                "Тестовому контуру нужен токен с опцией «Тестовый контур», "
                f"а передан токен категории «{self.token.kind.name}». "
                "См. https://dev.wildberries.ru/sandbox"
            )
        if is_test_token and not sandbox:
            raise WBConfigurationError(
                "Токен с опцией «Тестовый контур» работает только в тестовом "
                "контуре: создайте клиент с sandbox=True."
            )
        self.sandbox = sandbox
        self._session = Session(
            token.strip(),
            timeout=timeout,
            max_retries=max_retries,
            retry_backoff=retry_backoff,
            max_retry_wait=max_retry_wait,
            user_agent=user_agent,
            transport=transport,
        )
        self.general = General(self)
        self.items = Items(self)
        self.orders_fbs = OrdersFbs(self)
        self.orders_dbw = OrdersDbw(self)
        self.orders_dbs = OrdersDbs(self)
        self.in_store_pickup = InStorePickup(self)
        self.orders_fbw = OrdersFbw(self)
        self.promotion = Promotion(self)
        self.communications = Communications(self)
        self.rates = Rates(self)
        self.analytics = Analytics(self)
        self.reports = Reports(self)
        self.finances = Finances(self)
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
                f"Доступ запрещён: по токену недоступна категория методов API "
                f"«{scope.name}». Декодировать токен и посмотреть доступные "
                f"категории можно на портале разработчиков Wildberries.",
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

    @property
    def is_closed(self) -> bool:
        return self._session.is_closed

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
