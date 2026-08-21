from __future__ import annotations

from typing import TYPE_CHECKING

from .methods import (
    GetTariffsAcceptanceCoefficients,
    GetTariffsBox,
    GetTariffsCommission,
    GetTariffsPallet,
    GetTariffsReturns,
)
from .models import (
    Fee,
    ModelsAcceptanceCoefficient,
    RatesBoxResponse,
    RatesPalletResponse,
    ReturnRatesResponse,
)


if TYPE_CHECKING:
    from ..client import WBApi


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

    async def get_tariffs_acceptance_coefficients(
        self, *, warehouse_ids: str | None = None
    ) -> list[ModelsAcceptanceCoefficient]:
        """Тарифы на поставку

        :param warehouse_ids: ID складов.По умолчанию возвращаются данные по всем складам
        """
        return await GetTariffsAcceptanceCoefficients(warehouse_ids=warehouse_ids).emit(self._api)

    async def get_tariffs_box(self, *, date: str) -> RatesBoxResponse:
        """Тарифы для коробов

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await GetTariffsBox(date=date).emit(self._api)

    async def get_tariffs_commission(self, *, locale: str | None = None) -> Fee:
        """Комиссия по категориям товаров

        :param locale: Язык полей ответа `parentName` и `subjectName`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский
        """
        return await GetTariffsCommission(locale=locale).emit(self._api)

    async def get_tariffs_pallet(self, *, date: str) -> RatesPalletResponse:
        """Тарифы для монопаллет

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await GetTariffsPallet(date=date).emit(self._api)

    async def get_tariffs_returns(self, *, date: str) -> ReturnRatesResponse:
        """Тарифы на возврат

        :param date: Дата в формате ГГГГ-ММ-ДД
        """
        return await GetTariffsReturns(date=date).emit(self._api)
