from __future__ import annotations

from ..client.method import WBMethod
from .models import (
    Fee,
    ModelsAcceptanceCoefficient,
    RatesBoxResponse,
    RatesPalletResponse,
    ReturnRatesResponse,
)


class GetTariffsAcceptanceCoefficients(WBMethod[list[ModelsAcceptanceCoefficient]]):
    """Тарифы на поставку

    GET /api/tariffs/v1/acceptance/coefficients
    """

    __path__ = "/api/tariffs/v1/acceptance/coefficients"
    __http_method__ = "GET"
    __returns__ = list[ModelsAcceptanceCoefficient]
    __query_params__ = {"warehouse_ids": "warehouseIDs"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (10000, 6),
        "service": (10000, 6),
        "basic_secret": (10000, 6),
        "basic": (3600000, 1),
    }

    warehouse_ids: str | None = None
    """ID складов.По умолчанию возвращаются данные по всем складам"""


class GetTariffsBox(WBMethod[RatesBoxResponse]):
    """Тарифы для коробов

    GET /api/v1/tariffs/box
    """

    __path__ = "/api/v1/tariffs/box"
    __http_method__ = "GET"
    __returns__ = RatesBoxResponse
    __query_params__ = {"date": "date"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }

    date: str
    """Дата в формате ГГГГ-ММ-ДД"""


class GetTariffsCommission(WBMethod[Fee]):
    """Комиссия по категориям товаров

    GET /api/v1/tariffs/commission
    """

    __path__ = "/api/v1/tariffs/commission"
    __http_method__ = "GET"
    __returns__ = Fee
    __query_params__ = {"locale": "locale"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 2),
        "service": (60000, 2),
        "basic_secret": (60000, 2),
        "basic": (720000, 1),
    }

    locale: str | None = None
    """Язык полей ответа `parentName` и `subjectName`:   - `ru` — русский   - `en` — английский   -
    `zh` — китайский
    """


class GetTariffsPallet(WBMethod[RatesPalletResponse]):
    """Тарифы для монопаллет

    GET /api/v1/tariffs/pallet
    """

    __path__ = "/api/v1/tariffs/pallet"
    __http_method__ = "GET"
    __returns__ = RatesPalletResponse
    __query_params__ = {"date": "date"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }

    date: str
    """Дата в формате ГГГГ-ММ-ДД"""


class GetTariffsReturns(WBMethod[ReturnRatesResponse]):
    """Тарифы на возврат

    GET /api/v1/tariffs/return
    """

    __path__ = "/api/v1/tariffs/return"
    __http_method__ = "GET"
    __returns__ = ReturnRatesResponse
    __query_params__ = {"date": "date"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }

    date: str
    """Дата в формате ГГГГ-ММ-ДД"""
