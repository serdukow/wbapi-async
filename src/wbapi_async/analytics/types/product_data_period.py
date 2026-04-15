from ...types.base import BaseType


class ProductDataPeriod(BaseType):
    """Period for product data inventory report (format: YYYY-MM-DD, no earlier than 3 months ago)"""

    start: str
    end: str
