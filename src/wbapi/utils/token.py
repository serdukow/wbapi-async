from __future__ import annotations

import base64
import binascii
from enum import IntEnum
import json
from typing import Any, NamedTuple


__all__ = ("TokenKind", "Scope", "TokenInfo", "decode_token", "mask_token")


class TokenKind(IntEnum):
    """Категория токена — поле ``acc`` из payload."""

    BASIC = 1
    TEST = 2
    PERSONAL = 3
    SERVICE = 4


class Scope(IntEnum):
    """Позиция бита в маске ``s``, открывающая категорию методов."""

    CONTENT = 1
    ANALYTICS = 2
    PRICES = 3
    MARKETPLACE = 4
    STATISTICS = 5
    PROMOTION = 6
    FEEDBACKS = 7
    BUYER_CHAT = 9
    SUPPLIES = 10
    RETURNS = 11
    DOCUMENTS = 12
    FINANCE = 13
    USERS = 16
    READ_ONLY = 30


class TokenInfo(NamedTuple):
    kind: TokenKind | None
    seller_id: str | None
    expires_at: int | None
    scopes: frozenset[Scope]
    read_only: bool

    def allows(self, scope: Scope) -> bool:
        # An empty mask carries no scopes, so there is nothing to block on.
        return not self.scopes or scope in self.scopes


def mask_token(token: str) -> str:
    """Скрыть токен для логов и repr, оставив хвост для опознания."""
    if not token:
        return "<empty>"
    return f"***{token[-4:]}" if len(token) > 4 else "***"


def _payload(token: str) -> dict[str, Any] | None:
    parts = token.split(".")
    if len(parts) != 3:
        return None
    chunk = parts[1]
    chunk += "=" * (-len(chunk) % 4)
    try:
        raw = base64.urlsafe_b64decode(chunk)
        data = json.loads(raw)
    except (binascii.Error, UnicodeDecodeError, json.JSONDecodeError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def decode_token(token: str) -> TokenInfo:
    """Разобрать токен локально, без обращения к API и проверки подписи.

    Нечитаемый токен не считается ошибкой — решение остаётся за Wildberries.
    """
    data = _payload(token)
    if data is None:
        return TokenInfo(None, None, None, frozenset(), False)

    kind: TokenKind | None
    try:
        kind = TokenKind(int(data["acc"]))
    except (KeyError, TypeError, ValueError):
        kind = None

    mask = data.get("s")
    scopes: set[Scope] = set()
    if isinstance(mask, int):
        scopes = {scope for scope in Scope if mask >> scope & 1}

    seller_id = data.get("sid")
    expires_at = data.get("exp")

    return TokenInfo(
        kind=kind,
        seller_id=seller_id if isinstance(seller_id, str) else None,
        expires_at=expires_at if isinstance(expires_at, int) else None,
        scopes=frozenset(scopes - {Scope.READ_ONLY}),
        read_only=Scope.READ_ONLY in scopes,
    )
