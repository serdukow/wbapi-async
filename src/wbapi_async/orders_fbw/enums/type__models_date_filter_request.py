from enum import StrEnum


class TypeModelsDateFilterRequest(StrEnum):
    """Dates type:"""

    FACTDATE = "factDate"
    CREATEDATE = "createDate"
    SUPPLYDATE = "supplyDate"
    UPDATEDDATE = "updatedDate"
