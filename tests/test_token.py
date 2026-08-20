from __future__ import annotations

import pytest

from tests.conftest import make_token
from wbapi.utils import Scope, TokenKind, decode_token


@pytest.mark.parametrize(
    ("acc", "expected"),
    [
        (1, TokenKind.BASIC),
        (2, TokenKind.TEST),
        (3, TokenKind.PERSONAL),
        (4, TokenKind.SERVICE),
    ],
)
def test_category_read_from_acc(acc: int, expected: TokenKind) -> None:
    assert decode_token(make_token(acc=acc)).kind is expected


def test_unknown_category_is_none() -> None:
    assert decode_token(make_token(acc=99)).kind is None


def test_seller_id_and_expiry() -> None:
    info = decode_token(make_token(seller_id="abc-123", expires_at=1_800_000_000))
    assert info.seller_id == "abc-123"
    assert info.expires_at == 1_800_000_000


@pytest.mark.parametrize(
    "scope",
    [Scope.CONTENT, Scope.MARKETPLACE, Scope.FINANCE, Scope.USERS],
)
def test_single_scope_decoded(scope: Scope) -> None:
    info = decode_token(make_token(scopes=1 << scope))
    assert info.scopes == frozenset({scope})
    assert info.allows(scope)


def test_missing_scope_is_denied() -> None:
    info = decode_token(make_token(scopes=1 << Scope.CONTENT))
    assert not info.allows(Scope.FINANCE)


def test_read_only_bit() -> None:
    info = decode_token(make_token(scopes=1 << Scope.READ_ONLY))
    assert info.read_only
    assert Scope.READ_ONLY not in info.scopes


def test_token_without_mask_allows_everything() -> None:
    """Without a scope mask the library must not block anything."""
    info = decode_token(make_token())
    assert info.scopes == frozenset()
    assert all(info.allows(scope) for scope in Scope)


@pytest.mark.parametrize(
    "token",
    ["", "не-токен", "a.b", "a.b.c.d", "aaa.###.bbb", "aaa." + "!" * 8 + ".bbb"],
)
def test_malformed_token_does_not_raise(token: str) -> None:
    """An unreadable token must not crash the client; the API decides."""
    info = decode_token(token)
    assert info.kind is None
    assert info.scopes == frozenset()


def test_payload_that_is_not_an_object() -> None:
    import base64

    chunk = base64.urlsafe_b64encode(b'"a string"').decode().rstrip("=")
    assert decode_token(f"aaa.{chunk}.bbb").kind is None


def test_several_scopes_at_once() -> None:
    mask = (1 << Scope.CONTENT) | (1 << Scope.PROMOTION) | (1 << Scope.RETURNS)
    info = decode_token(make_token(scopes=mask))
    assert info.scopes == frozenset({Scope.CONTENT, Scope.PROMOTION, Scope.RETURNS})
