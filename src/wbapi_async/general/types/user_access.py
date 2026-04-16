from pydantic import Field

from ...types.base import BaseType
from .access_item import AccessItem


class UserAccess(BaseType):
    user_id: int | None = Field(None, alias="userId")
    access: list[AccessItem] | None = Field(None, alias="access")
