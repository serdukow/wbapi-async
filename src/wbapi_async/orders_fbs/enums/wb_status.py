from enum import StrEnum


class WbStatus(StrEnum):
    """Assembly order status set by WB system"""

    WAITING = "waiting"
    SORTED = "sorted"
    SOLD = "sold"
    CANCELED = "canceled"
    CANCELED_BY_CLIENT = "canceled_by_client"
    DECLINED_BY_CLIENT = "declined_by_client"
    DEFECT = "defect"
    READY_FOR_PICKUP = "ready_for_pickup"
    POSTPONED_DELIVERY = "postponed_delivery"
    ACCEPTED_BY_CARRIER = "accepted_by_carrier"
    SENT_TO_CARRIER = "sent_to_carrier"
