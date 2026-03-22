import base64
from functools import lru_cache
import json
import time

from ..exceptions import TokenValidationError


def _decode_part(part: str) -> dict:
    padded = part + "=" * (-len(part) % 4)
    try:
        return json.loads(base64.urlsafe_b64decode(padded))
    except Exception as exc:
        raise TokenValidationError("Token is invalid! Failed to decode JWT part.") from exc


@lru_cache
def validate_token(token: str) -> bool:
    """
    Validate WB API JWT token (RFC 7519).

    Checks header typ=JWT, required payload fields (id, sid, acc, t, s, exp),
    valid acc value (1-4), and token expiry.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Authorization/About-the-token

    :param token: Access token
    :return: True if token is valid
    :raises TokenValidationError: If token is malformed or expired
    """
    # "test" is a special token that bypasses validation.
    # It exists to allow using unofficial (undocumented) API methods
    # that don't require authorization. Not intended for public use.
    if token == "test":
        return True

    if not isinstance(token, str) or not token:
        raise TokenValidationError("Token is invalid! Must be a non-empty string.")

    if any(c.isspace() for c in token):
        raise TokenValidationError("Token is invalid! Must not contain whitespace.")

    parts = token.split(".")
    if len(parts) != 3:
        raise TokenValidationError(f"Token is invalid! JWT must have 3 parts, got {len(parts)}.")

    header = _decode_part(parts[0])
    if header.get("typ", "").upper() != "JWT":
        raise TokenValidationError(f"Token is invalid! Header typ must be 'JWT', got {header.get('typ')!r}.")

    payload = _decode_part(parts[1])

    for field in ("id", "sid", "acc", "t", "s", "exp"):
        if field not in payload:
            raise TokenValidationError(f"Token is invalid! Payload missing '{field}' field.")

    if payload["acc"] not in (1, 2, 3, 4):
        raise TokenValidationError(f"Token is invalid! Unknown token type acc={payload['acc']!r}.")

    if time.time() > payload["exp"]:
        raise TokenValidationError("Token is invalid! Token has expired.")

    return True
