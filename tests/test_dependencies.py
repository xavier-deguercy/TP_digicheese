import pytest
from fastapi import HTTPException

from src.utils.dependencies import get_current_user_api_key, require_roles
from src.repositories.utilisateur_repository import UtilisateurRepository


class DummyRole:
    def __init__(self, libelle_role: str):
        self.libelle_role = libelle_role


class DummyUser:
    def __init__(self, role: DummyRole):
        self.role = role


def test_get_current_user_api_key_disabled_auth(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "true")

    assert get_current_user_api_key(api_key=None, db=None) is None


def test_get_current_user_api_key_missing_key(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")

    with pytest.raises(HTTPException) as excinfo:
        get_current_user_api_key(api_key=None, db=None)

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "X-API-Key manquante"


def test_get_current_user_api_key_invalid_key(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")
    monkeypatch.setattr(UtilisateurRepository, "get_by_api_key", lambda db, api_key: None)

    with pytest.raises(HTTPException) as excinfo:
        get_current_user_api_key(api_key="bad-key", db=object())

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "X-API-Key invalide"


def test_get_current_user_api_key_valid(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")
    user = DummyUser(role=DummyRole("ADMIN"))
    monkeypatch.setattr(UtilisateurRepository, "get_by_api_key", lambda db, api_key: user)

    result = get_current_user_api_key(api_key="valid-key", db=object())

    assert result is user


def test_require_roles_allows_authorized_role(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")
    dependency = require_roles("ADMIN", "MANAGER")
    user = DummyUser(role=DummyRole("ADMIN"))

    assert dependency(current_user=user) is user


def test_require_roles_forbidden_for_unauthorized_role(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")
    dependency = require_roles("ADMIN")
    user = DummyUser(role=DummyRole("USER"))

    with pytest.raises(HTTPException) as excinfo:
        dependency(current_user=user)

    assert excinfo.value.status_code == 403
    assert excinfo.value.detail == "Accès interdit"


def test_require_roles_disabled_auth_returns_user(monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "true")
    dependency = require_roles("ADMIN")
    user = DummyUser(role=DummyRole("USER"))

    assert dependency(current_user=user) is user
