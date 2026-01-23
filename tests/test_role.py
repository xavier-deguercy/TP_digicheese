from fastapi import Response
from fastapi.testclient import TestClient
import pytest

ROLE_ENDPOINT = "/roles"

@pytest.fixture
def role_data():
    """Données de test pour créer un rôle."""
    return {"libelle_role": "ADMIN"}


def test_get_all_roles(client: TestClient):
    """Au début, la liste doit être vide."""
    response: Response = client.get(ROLE_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_role(client: TestClient, role_data):
    """Créer un rôle."""
    response: Response = client.post(ROLE_ENDPOINT, json=role_data)
    assert response.status_code == 201

    data = response.json()
    assert "id_role" in data
    assert data["libelle_role"] == role_data["libelle_role"]


def test_get_role_by_id(client: TestClient, role_data):
    """Récupérer un rôle par ID."""
    created = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = created["id_role"]

    response: Response = client.get(f"{ROLE_ENDPOINT}/{role_id}")
    assert response.status_code == 200
    assert response.json()["id_role"] == role_id
    assert response.json()["libelle_role"] == role_data["libelle_role"]


def test_patch_role_by_id(client: TestClient, role_data):
    """Modifier partiellement un rôle."""
    created = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = created["id_role"]

    new_data = {"libelle_role": "OP COLIS"}
    response: Response = client.patch(f"{ROLE_ENDPOINT}/{role_id}", json=new_data)
    assert response.status_code == 200
    assert response.json()["libelle_role"] == "OP COLIS"


def test_delete_role_by_id(client: TestClient, role_data):
    """Supprimer un rôle."""
    created = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = created["id_role"]

    response: Response = client.delete(f"{ROLE_ENDPOINT}/{role_id}")
    assert response.status_code == 200

    response: Response = client.get(f"{ROLE_ENDPOINT}/{role_id}")
    assert response.status_code == 404
