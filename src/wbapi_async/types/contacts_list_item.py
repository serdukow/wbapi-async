from pydantic import Field

from .base import BaseType


class ContactsListItem(BaseType):
    """Contacts List"""

    comment: str | None = Field(None)
    phone: str | None = Field(None)
