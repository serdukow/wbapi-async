from ...methods.base import WbMethod
from ...types import RequestLimit, SizeDataItem


class GetSizeData(WbMethod):
    """
    Forms a dataset for inventory by the size of the product. Possible cases: 1. The product has
    dimensionsand `"includeOffice":true`, then the response body will contain data on the inventory
    foreach of the sizes with nested details by warehouse. 2. The product has dimensions and
    `"includeOffice":false`,then the response body will contain data on the inventory for each of
    thesizes without nested details by warehouse. 3. The product has no size and `"include
    Office":true`,then the response body will contain details by warehouse without data on the
    inventoryfor each of the sizes. 4. The product has no size and `"include Office":false`, then
    theresponse body will be empty. `The product has no size` means the size of the product is the
    sameand has `"techSize":"0"`. In responses of the method for getting data on
    [products](/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post),
    suchproducts have `hasSizes':false`. The data on the seller's warehouses are in an aggregated
    form— for all of them together without detailing specific warehouses — and responses contain
    `"regionName":"Маркетплейс"`and `"officeName":""` in such cases.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1sizes/post
    """

    __return__ = SizeDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/sizes"
    __http_method__ = "POST"
    __data_key__ = "data.offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
