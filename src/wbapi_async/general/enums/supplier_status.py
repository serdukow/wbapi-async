from enum import StrEnum


class SupplierStatus(StrEnum):
    """Assembly order status set by the seller"""

    NEW = "new"
    CONFIRM = "confirm"
    COMPLETE = "complete"
    CANCEL = "cancel"
