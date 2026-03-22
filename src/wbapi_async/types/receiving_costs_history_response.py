from pydantic import Field

from .base import BaseType


class ReceivingCostsHistoryResponse(BaseType):
    """Receiving Costs History"""

    upd_num: int | None = Field(None, alias="updNum")
    upd_time: str | None = Field(None, alias="updTime")
    upd_sum: int | None = Field(None, alias="updSum")
    advert_id: int | None = Field(None, alias="advertId")
    camp_name: str | None = Field(None, alias="campName")
    advert_type: int | None = Field(None, alias="advertType")
    payment_type: str | None = Field(None, alias="paymentType")
    advert_status: int | None = Field(None, alias="advertStatus")
