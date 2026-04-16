from pydantic import Field

from ...types.base import BaseType
from ..enums.type__models_date_filter_request import TypeModelsDateFilterRequest


class ModelsDateFilterRequest(BaseType):
    from_: str | None = Field(None, alias="from")
    till: str | None = Field(None)
    type_: TypeModelsDateFilterRequest = Field(alias="type")
