from fastapi.testclient import TestClient


def _create_user_with_role(client: TestClient, role_name: str) -> str:
    role_response = client.post("/roles", json={"libelle_role": role_name})
    assert role_response.status_code == 201, role_response.text

    user_response = client.post(
        "/utilisateurs",
        json={
            "nom_user": "Operateur",
            "prenom_user": "Colis",
            "username": "op.colis",
            "password": "test-password",
            "id_role": role_response.json()["id_role"],
        },
    )
    assert user_response.status_code == 201, user_response.text
    return user_response.json()["api_key"]


def test_op_colis_seed_role_can_access_colis_routes(client: TestClient, monkeypatch):
    api_key = _create_user_with_role(client, "OP-COLIS")
    monkeypatch.setenv("DISABLE_AUTH", "false")

    response = client.get("/commune", headers={"X-API-Key": api_key})

    assert response.status_code == 200, response.text


def test_auth_enabled_rejects_missing_api_key(client: TestClient, monkeypatch):
    monkeypatch.setenv("DISABLE_AUTH", "false")

    response = client.get("/commune")

    assert response.status_code == 401


def test_dev_api_key_route_is_not_exposed(client: TestClient):
    assert client.get("/dev/api-key/1").status_code == 404
    assert "/dev/api-key/{user_id}" not in client.get("/openapi.json").json()["paths"]
