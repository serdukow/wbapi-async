from pydantic import Field

from ...types.base import BaseType


class Invite(BaseType):
    phone_number: str = Field(alias="phoneNumber")
    position: str | None = Field(None)
