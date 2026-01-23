from fastapi import Response
from fastapi.testclient import TestClient
import pytest

CLIENT_ENDPOINT = "/clients"
ADRESSE_ENDPOINT = "/adresses"
COMMUNE_ENDPOINT = "/communes"

@pytest.fixture
def commune_data():
    return {
        "dep": "34",
        "cp": "34000",
        "ville": "Montpellier",
    }

@pytest.fixture
def adresse_data():
    # id_commune ajouté après création de la commune
    return {
        "rue": "1 rue des Tests",
        "compAdresse": "Bât A",
    }

@pytest.fixture
def client_data():
    # adresse1_client ajouté après création de l'adresse
    return {
        "email_client": "client@test.com",
        "nom_client": "Didier",
        "prenom_client": "Francis",
        "telephone_client": "0627000000",
        # adresse2_client optionnel
    }


def _create_commune(client: TestClient, commune_data: dict) -> dict:
    res = client.post(COMMUNE_ENDPOINT, json=commune_data)
    assert res.status_code in (200, 201), res.text
    return res.json()


def _create_adresse(client: TestClient, adresse_data: dict, id_commune: int) -> dict:
    payload = {**adresse_data, "id_commune": id_commune}
    res = client.post(ADRESSE_ENDPOINT, json=payload)
    assert res.status_code in (200, 201), res.text
    return res.json()


def test_get_all_clients_empty(client: TestClient):
    response: Response = client.get(CLIENT_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_client(client: TestClient, commune_data, adresse_data, client_data):
    # créer une commune + adresse (FK obligatoire pour adresse, puis adresse obligatoire pour client)
    commune = _create_commune(client, commune_data)
    id_commune = commune["id_commune"]

    adresse = _create_adresse(client, adresse_data, id_commune=id_commune)
    id_adresse = adresse["id_adresse"]

    payload = {**client_data, "adresse1_client": id_adresse}
    response: Response = client.post(CLIENT_ENDPOINT, json=payload)

    assert response.status_code == 201, response.text
    data = response.json()

    assert "id_client" in data
    assert data["email_client"] == client_data["email_client"]
    assert data["nom_client"] == client_data["nom_client"]
    assert data["prenom_client"] == client_data["prenom_client"]
    assert data["telephone_client"] == client_data["telephone_client"]
    assert data["adresse1_client"] == id_adresse


def test_get_client_by_id(client: TestClient, commune_data, adresse_data, client_data):
    commune = _create_commune(client, commune_data)
    adresse = _create_adresse(client, adresse_data, id_commune=commune["id_commune"])

    created = client.post(CLIENT_ENDPOINT, json={**client_data, "adresse1_client": adresse["id_adresse"]}).json()
    client_id = created["id_client"]

    response: Response = client.get(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 200
    assert response.json()["id_client"] == client_id


def test_patch_client_by_id(client: TestClient, commune_data, adresse_data, client_data):
    commune = _create_commune(client, commune_data)
    adresse = _create_adresse(client, adresse_data, id_commune=commune["id_commune"])

    created = client.post(CLIENT_ENDPOINT, json={**client_data, "adresse1_client": adresse["id_adresse"]}).json()
    client_id = created["id_client"]

    patch_payload = {"prenom_client": "Jean"}
    response: Response = client.patch(f"{CLIENT_ENDPOINT}/{client_id}", json=patch_payload)

    assert response.status_code == 200, response.text
    assert response.json()["prenom_client"] == "Jean"


def test_delete_client_by_id(client: TestClient, commune_data, adresse_data, client_data):
    commune = _create_commune(client, commune_data)
    adresse = _create_adresse(client, adresse_data, id_commune=commune["id_commune"])

    created = client.post(CLIENT_ENDPOINT, json={**client_data, "adresse1_client": adresse["id_adresse"]}).json()
    client_id = created["id_client"]

    response: Response = client.delete(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 200, response.text

    response: Response = client.get(f"{CLIENT_ENDPOINT}/{client_id}")
    assert response.status_code == 404
