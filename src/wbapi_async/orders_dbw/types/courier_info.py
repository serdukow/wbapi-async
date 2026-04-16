from pydantic import Field

from ...types.base import BaseType
from .contacts import Contacts


class CourierInfo(BaseType):
    """Courier info"""

    contacts: Contacts | None = Field(None, alias="contacts")
    must_be_assigned: bool | None = Field(None, alias="mustBeAssigned")
    updated_at: str | None = Field(None, alias="updatedAt")
