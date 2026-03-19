from typing import Any

from pydantic import BaseModel, Field


_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


class Headers(BaseModel):
    model_config = {"populate_by_name": True}

    accept: str = Field("application/json;charset=utf-8", alias="Accept")
    content_type: str = Field("application/json", alias="Content-Type")
    authorization: str | None = Field(None, alias="Authorization")
    user_agent: str = Field(_DEFAULT_UA, alias="User-Agent")

    def set_token(self, token: str) -> None:
        self.authorization = f"Bearer {token}"

    def model_dump(self, **_kwargs: Any) -> dict[str, str]:  # type: ignore[override]
        headers: dict[str, str] = {
            "Accept": self.accept,
            "Content-Type": self.content_type,
            "User-Agent": self.user_agent,
        }
        if self.authorization is not None:
            headers["Authorization"] = self.authorization
        return headers
