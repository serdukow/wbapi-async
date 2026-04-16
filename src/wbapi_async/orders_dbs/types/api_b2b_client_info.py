from pydantic import Field

from ...types.base import BaseType


class ApiB2BClientInfo(BaseType):
    """B2B buyer data"""

    inn: str | None = Field(None, alias="inn")
    kpp: str | None = Field(None, alias="kpp")
    org_name: str | None = Field(None, alias="orgName")
