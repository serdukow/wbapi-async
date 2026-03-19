from typing import Any

from pydantic import BaseModel, Field


class Headers(BaseModel):
    model_config = {"populate_by_name": True}

    accept: str = Field("application/json;charset=utf-8", alias="Accept")
    content_type: str = Field("application/json", alias="Content-Type")
    authorization: str = Field("Bearer", alias="Authorization")

    def set_token(self, token: str) -> None:
        self.authorization = f"Bearer {token}"

    def model_dump(self, **_kwargs: Any) -> dict[str, str]:  # type: ignore[override]
        return {
            "Accept": self.accept,
            "Content-Type": self.content_type,
            "Authorization": self.authorization,
        }
