import pytest
import src.services.utilisateur_service as utilisateur_service
from src.services.utilisateur_service import UtilisateurService


@pytest.mark.critical
def test_traitement_create_hashes_and_sets_api_key(monkeypatch):
    svc = UtilisateurService()
    monkeypatch.setattr(utilisateur_service, "hash_password", lambda p: f"hashed:{p}")
    monkeypatch.setattr(utilisateur_service.secrets, "token_hex", lambda n: "token123")

    data = {"username": "u1", "password": "pass", "id_role": 1}
    out = svc._UtilisateurService__traitement_create(data.copy())

    assert "password" not in out
    assert out["hashed_password"] == "hashed:pass"
    assert out["api_key"] == "token123"


@pytest.mark.critical
def test_traitement_patch_adds_hash_when_password(monkeypatch):
    svc = UtilisateurService()
    monkeypatch.setattr(utilisateur_service, "hash_password", lambda p: f"hashed:{p}")

    data = {"password": "newpass"}
    out = svc._UtilisateurService__traitement_patch(data.copy())

    assert "password" not in out
    assert out["hashed_password"] == "hashed:newpass"


def test_traitement_patch_no_password():
    svc = UtilisateurService()
    data = {"prenom_user": "Jane"}
    out = svc._UtilisateurService__traitement_patch(data.copy())

    assert out == data
