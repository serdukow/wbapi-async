from __future__ import annotations

from typing import TYPE_CHECKING

from .methods import (
    TariffsBox,
    TariffsCommission,
    TariffsPallet,
    TariffsReturn,
    TariffsV1AcceptanceCoefficients,
)
from .models import (
    Fee,
    ModelsAcceptanceCoefficient,
    RatesBoxResponse,
    RatesPalletResponse,
    ReturnRatesResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


class Rates:
    """Тарифы.

    Узнать больше о тарифах можно в справочном центре

    В разделе описаны методы получения:
      1. Комиссий
      2. Тарифов на поставку
      3. Тарифов на остаток
      4. Тарифов на возврат товаров продавцу
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def tariffs_box(self, *, date: str) -> RatesBoxResponse:
        """Тарифы для коробов

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await TariffsBox(date=date).emit(self._api)

    async def tariffs_commission(self, *, locale: str | None = None) -> Fee:
        """Комиссия по категориям товаров

        :param locale: Язык полей ответа `parentName` и `subjectName`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский
        """
        return await TariffsCommission(locale=locale).emit(self._api)

    async def tariffs_pallet(self, *, date: str) -> RatesPalletResponse:
        """Тарифы для монопаллет

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await TariffsPallet(date=date).emit(self._api)

    async def tariffs_return(self, *, date: str) -> ReturnRatesResponse:
        """Тарифы на возврат

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await TariffsReturn(date=date).emit(self._api)

    async def tariffs_v1_acceptance_coefficients(
        self, *, warehouse_ids: str | None = None
    ) -> list[ModelsAcceptanceCoefficient]:
        """Тарифы на поставку

        :param warehouse_ids: ID складов.По умолчанию возвращаются данные по всем складам
        """
        return await TariffsV1AcceptanceCoefficients(warehouse_ids=warehouse_ids).emit(self._api)
