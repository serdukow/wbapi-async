_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


class Headers:
    def __init__(self) -> None:
        self.accept = "application/json;charset=utf-8"
        self.content_type = "application/json"
        self.authorization: str | None = None
        self.user_agent = _DEFAULT_UA

    def set_token(self, token: str) -> None:
        self.authorization = f"Bearer {token}"

    def as_dict(self) -> dict[str, str]:
        headers: dict[str, str] = {
            "Accept": self.accept,
            "Content-Type": self.content_type,
            "User-Agent": self.user_agent,
        }
        if self.authorization is not None:
            headers["Authorization"] = self.authorization
        return headers
