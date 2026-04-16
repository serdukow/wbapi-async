from pydantic import Field

from ...types.base import BaseType


class ContactsListItem(BaseType):
    """Contacts List"""

    comment: str | None = Field(None, alias="comment")
    phone: str | None = Field(None, alias="phone")
