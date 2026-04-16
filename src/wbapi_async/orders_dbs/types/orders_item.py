from pydantic import Field

from ...types.base import BaseType


class OrdersItem(BaseType):
    customs_declaration: str = Field(alias="customsDeclaration")
    order_id: int = Field(alias="orderId")
