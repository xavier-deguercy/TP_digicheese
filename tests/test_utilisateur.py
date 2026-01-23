from fastapi import Response
from fastapi.testclient import TestClient
import pytest

UTILISATEUR_ENDPOINT = "/utilisateurs"
ROLE_ENDPOINT = "/roles"


@pytest.fixture
def role_data():
    return {"libelle_role": "ADMIN"}


@pytest.fixture
def user_data():
    return {
        "nom_user": "Doe",
        "prenom_user": "John",
        "username": "john.doe",
        "password": "secret123",
    }


def test_get_all_users_empty(client: TestClient):
    response: Response = client.get(UTILISATEUR_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_user(client: TestClient, role_data, user_data):
    # créer un rôle (FK obligatoire)
    role = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = role["id_role"]

    payload = {**user_data, "id_role": role_id}
    response: Response = client.post(UTILISATEUR_ENDPOINT, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id_user" in data
    assert data["nom_user"] == user_data["nom_user"]
    assert data["prenom_user"] == user_data["prenom_user"]
    assert data["username"] == user_data["username"]
    assert "password" not in data
    assert "hashed_password" not in data


def test_get_user_by_id(client: TestClient, role_data, user_data):
    role = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = role["id_role"]

    created = client.post(UTILISATEUR_ENDPOINT, json={**user_data, "id_role": role_id}).json()
    user_id = created["id_user"]

    response: Response = client.get(f"{UTILISATEUR_ENDPOINT}/{user_id}")
    assert response.status_code == 200
    assert response.json()["id_user"] == user_id


def test_patch_user_by_id(client: TestClient, role_data, user_data):
    role = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = role["id_role"]

    created = client.post(UTILISATEUR_ENDPOINT, json={**user_data, "id_role": role_id}).json()
    user_id = created["id_user"]

    patch_payload = {"prenom_user": "Jane"}
    response: Response = client.patch(f"{UTILISATEUR_ENDPOINT}/{user_id}", json=patch_payload)
    assert response.status_code == 200
    assert response.json()["prenom_user"] == "Jane"


def test_delete_user_by_id(client: TestClient, role_data, user_data):
    role = client.post(ROLE_ENDPOINT, json=role_data).json()
    role_id = role["id_role"]

    created = client.post(UTILISATEUR_ENDPOINT, json={**user_data, "id_role": role_id}).json()
    user_id = created["id_user"]

    response: Response = client.delete(f"{UTILISATEUR_ENDPOINT}/{user_id}")
    assert response.status_code == 200

    response: Response = client.get(f"{UTILISATEUR_ENDPOINT}/{user_id}")
    assert response.status_code == 404
