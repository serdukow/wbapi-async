from pydantic import Field

from ...types.base import BaseType


class ContactsItem(BaseType):
    comment: str | None = Field(None)
    phone: str | None = Field(None)
