from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    AccountBalance,
    DocumentsCategories,
    DocumentsDownload,
    DocumentsDownloadAll,
    DocumentsList,
    FinanceV1AcquiringDetailedCreate,
    FinanceV1AcquiringDetailedReportIdCreate,
    FinanceV1AcquiringList,
    FinanceV1SalesReportsDetailedCreate,
    FinanceV1SalesReportsDetailedReportIdCreate,
    FinanceV1SalesReportsList,
)
from .models import (
    AccountBalanceResponse,
    AcquiringReportListRes,
    AcquiringReportsDetailedRes,
    DocumentsDownloadAllParamsItem,
    GetCategories,
    GetDoc,
    GetDocs,
    GetList,
    SalesReportListRes,
    SalesReportsDetailedRes,
)


if TYPE_CHECKING:
    from ...client import WBApi


class Finances:
    """Документы и бухгалтерия.

    Узнать больше о документах и бухгалтерии можно в справочном центре

    Просмотр баланса, финансовых отчётов и документов продавца.
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def account_balance(self) -> AccountBalanceResponse:
        """Получить баланс продавца"""
        return await AccountBalance().emit(self._api)

    async def documents_categories(self, *, locale: str | None = None) -> GetCategories:
        """Категории документов

        :param locale: Язык поля `title`:   - `ru` — русский   - `en` — английский   - `zh` — китайский
        """
        return await DocumentsCategories(locale=locale).emit(self._api)

    async def documents_download(self, *, extension: str, service_name: str) -> GetDoc:
        """Получить документ

        :param extension: Формат документа
        :param service_name: Уникальный ID документа
        """
        return await DocumentsDownload(extension=extension, service_name=service_name).emit(self._api)

    async def documents_download_all(
        self, *, params: list[DocumentsDownloadAllParamsItem] | None = None
    ) -> GetDocs:
        """Получить документы"""
        return await DocumentsDownloadAll(params=params).emit(self._api)

    async def documents_list(
        self,
        *,
        begin_time: str | None = None,
        category: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        locale: str | None = None,
        offset: int | None = None,
        order: str | None = None,
        service_name: str | None = None,
        sort: str | None = None,
        auto_paginate: bool = False,
    ) -> GetList | list[Any]:
        """Список документов

        :param begin_time: Начало периода. Только вместе с `endTime`
        :param category: ID категории документов из поля `name`
        :param end_time: Конец периода. Только вместе с `beginTime`
        :param limit: Максимальное количество строк ответа
        :param locale: Язык поля `category`:   - `ru` — русский   - `en` — английский   - `zh` — китайский
        :param offset: После какой строки выдавать данные
        :param order: Сортировка:   - `desc` — по убыванию   - `asc` — по возрастанию  Только вместе с
            `sort`
        :param service_name: Уникальный ID документа
        :param sort: Сортировка:   - `date` — по дате создания документа   - `category` — по категории
            (только при `locale=ru`)  Только вместе с `order`
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = DocumentsList(
            begin_time=begin_time,
            category=category,
            end_time=end_time,
            limit=limit,
            locale=locale,
            offset=offset,
            order=order,
            service_name=service_name,
            sort=sort,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_documents_list(
        self,
        *,
        begin_time: str | None = None,
        category: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        locale: str | None = None,
        offset: int | None = None,
        order: str | None = None,
        service_name: str | None = None,
        sort: str | None = None,
    ) -> AsyncIterator[Any]:
        """Список документов — постранично, по одной записи.

        :param begin_time: Начало периода. Только вместе с `endTime`
        :param category: ID категории документов из поля `name`
        :param end_time: Конец периода. Только вместе с `beginTime`
        :param limit: Максимальное количество строк ответа
        :param locale: Язык поля `category`:   - `ru` — русский   - `en` — английский   - `zh` — китайский
        :param offset: После какой строки выдавать данные
        :param order: Сортировка:   - `desc` — по убыванию   - `asc` — по возрастанию  Только вместе с
            `sort`
        :param service_name: Уникальный ID документа
        :param sort: Сортировка:   - `date` — по дате создания документа   - `category` — по категории
            (только при `locale=ru`)  Только вместе с `order`
        """
        async for item in DocumentsList(
            begin_time=begin_time,
            category=category,
            end_time=end_time,
            limit=limit,
            locale=locale,
            offset=offset,
            order=order,
            service_name=service_name,
            sort=sort,
        ).stream(self._api):
            yield item

    async def finance_v1_acquiring_detailed_create(
        self,
        *,
        date_from: str,
        date_to: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
        auto_paginate: bool = False,
    ) -> list[AcquiringReportsDetailedRes] | list[Any]:
        """Детализации к отчётам об издержках на приём платежей за период

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1AcquiringDetailedCreate(
            date_from=date_from, date_to=date_to, fields=fields, limit=limit, rrd_id=rrd_id
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_acquiring_detailed_create(
        self,
        *,
        date_from: str,
        date_to: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Детализации к отчётам об издержках на приём платежей за период — постранично, по одной записи.

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        """
        async for item in FinanceV1AcquiringDetailedCreate(
            date_from=date_from, date_to=date_to, fields=fields, limit=limit, rrd_id=rrd_id
        ).stream(self._api):
            yield item

    async def finance_v1_acquiring_detailed_report_id_create(
        self,
        *,
        report_id: str | int,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
        auto_paginate: bool = False,
    ) -> list[AcquiringReportsDetailedRes] | list[Any]:
        """Детализации к отчётам об издержках на приём платежей по ID отчётов

        :param report_id: ID отчёта
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1AcquiringDetailedReportIdCreate(
            report_id=report_id, fields=fields, limit=limit, rrd_id=rrd_id
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_acquiring_detailed_report_id_create(
        self,
        *,
        report_id: str | int,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Детализации к отчётам об издержках на приём платежей по ID отчётов — постранично, по одной записи.

        :param report_id: ID отчёта
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        """
        async for item in FinanceV1AcquiringDetailedReportIdCreate(
            report_id=report_id, fields=fields, limit=limit, rrd_id=rrd_id
        ).stream(self._api):
            yield item

    async def finance_v1_acquiring_list(
        self,
        *,
        date_from: str,
        date_to: str,
        limit: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> list[AcquiringReportListRes] | list[Any]:
        """Список отчётов об издержках на приём платежей

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param limit: Количество отчётов в ответе
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1AcquiringList(date_from=date_from, date_to=date_to, limit=limit, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_acquiring_list(
        self, *, date_from: str, date_to: str, limit: int | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Список отчётов об издержках на приём платежей — постранично, по одной записи.

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param limit: Количество отчётов в ответе
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in FinanceV1AcquiringList(
            date_from=date_from, date_to=date_to, limit=limit, offset=offset
        ).stream(self._api):
            yield item

    async def finance_v1_sales_reports_detailed_create(
        self,
        *,
        date_from: str,
        date_to: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        period: str | None = None,
        rrd_id: int | None = None,
        auto_paginate: bool = False,
    ) -> list[SalesReportsDetailedRes] | list[Any]:
        """Детализации к отчётам реализации за период

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param period: Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1SalesReportsDetailedCreate(
            date_from=date_from, date_to=date_to, fields=fields, limit=limit, period=period, rrd_id=rrd_id
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_sales_reports_detailed_create(
        self,
        *,
        date_from: str,
        date_to: str,
        fields: list[str] | None = None,
        limit: int | None = None,
        period: str | None = None,
        rrd_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Детализации к отчётам реализации за период — постранично, по одной записи.

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param period: Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        """
        async for item in FinanceV1SalesReportsDetailedCreate(
            date_from=date_from, date_to=date_to, fields=fields, limit=limit, period=period, rrd_id=rrd_id
        ).stream(self._api):
            yield item

    async def finance_v1_sales_reports_detailed_report_id_create(
        self,
        *,
        report_id: str | int,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
        auto_paginate: bool = False,
    ) -> list[SalesReportsDetailedRes] | list[Any]:
        """Детализации к отчётам реализации по ID отчётов

        :param report_id: ID отчёта.Для ежедневных отчётов вместо стандартной десериализации рекомендуем
            использовать нестандартные библиотеки с поддержкой BigInt
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1SalesReportsDetailedReportIdCreate(
            report_id=report_id, fields=fields, limit=limit, rrd_id=rrd_id
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_sales_reports_detailed_report_id_create(
        self,
        *,
        report_id: str | int,
        fields: list[str] | None = None,
        limit: int | None = None,
        rrd_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Детализации к отчётам реализации по ID отчётов — постранично, по одной записи.

        :param report_id: ID отчёта.Для ежедневных отчётов вместо стандартной десериализации рекомендуем
            использовать нестандартные библиотеки с поддержкой BigInt
        :param fields: Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все
            поля
        :param limit: Количество строк в ответе
        :param rrd_id: ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
            `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
        """
        async for item in FinanceV1SalesReportsDetailedReportIdCreate(
            report_id=report_id, fields=fields, limit=limit, rrd_id=rrd_id
        ).stream(self._api):
            yield item

    async def finance_v1_sales_reports_list(
        self,
        *,
        date_from: str,
        date_to: str,
        limit: int | None = None,
        offset: int | None = None,
        period: str | None = None,
        auto_paginate: bool = False,
    ) -> list[SalesReportListRes] | list[Any]:
        """Список отчётов реализации

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param limit: Количество отчётов в ответе
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param period: Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FinanceV1SalesReportsList(
            date_from=date_from, date_to=date_to, limit=limit, offset=offset, period=period
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_finance_v1_sales_reports_list(
        self,
        *,
        date_from: str,
        date_to: str,
        limit: int | None = None,
        offset: int | None = None,
        period: str | None = None,
    ) -> AsyncIterator[Any]:
        """Список отчётов реализации — постранично, по одной записи.

        :param date_from: Начальная дата отчёта.Можно передать дату или дату со временем. Время можно
            указывать с точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339,
            в …
        :param date_to: Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со
            временем. Время можно указывать с точностью до секунд или миллисекунд.Время передаё
            …
        :param limit: Количество отчётов в ответе
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param period: Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные
        """
        async for item in FinanceV1SalesReportsList(
            date_from=date_from, date_to=date_to, limit=limit, offset=offset, period=period
        ).stream(self._api):
            yield item
