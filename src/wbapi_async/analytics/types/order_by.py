from pydantic import Field as PydanticField

from ...types.base import BaseType
from ..enums.field import Field
from ..enums.mode import Mode


class OrderBy(BaseType):
    """Sorting parameters"""

    field: Field = PydanticField()
    mode: Mode = PydanticField()
