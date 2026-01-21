# tests/test_conditionnement_crud.py

from fastapi import Response
from fastapi.testclient import TestClient
import pytest
from decimal import Decimal, InvalidOperation

CONDIT_ENDPOINT = "/conditionnements/"


def norm_price(v) -> Decimal:
    """
    Normalise un prix venant du JSON (int/float/str/Decimal) vers Decimal.
    Exemple: 0, "0", "0.0000" -> Decimal("0.0000")
    """
    try:
        return Decimal(str(v))
    except (InvalidOperation, TypeError):
        raise AssertionError(f"Valeur prix_condit invalide: {v!r}")


@pytest.fixture
def conditionnement_data():
    return {
        "lib_condit": "Sachet 250g",
        "poids_condit": 250,
        "prix_condit": 0,
        "ordre_imp": 1,
    }


def test_get_all_conditionnements(client: TestClient):
    response: Response = client.get(CONDIT_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_conditionnement(client: TestClient, conditionnement_data):
    response: Response = client.post(CONDIT_ENDPOINT, json=conditionnement_data)
    assert response.status_code == 201

    data = response.json()
    assert "id_condit" in data
    del data["id_condit"]

    # Compare tous les champs sauf prix_condit en égalité stricte (style prof)
    expected = conditionnement_data.copy()

    # Sépare la comparaison du prix (car formatage "0" vs "0.0000")
    assert data["lib_condit"] == expected["lib_condit"]
    assert data["poids_condit"] == expected["poids_condit"]
    assert data["ordre_imp"] == expected["ordre_imp"]
    assert norm_price(data["prix_condit"]) == norm_price(expected["prix_condit"])


def test_get_conditionnement_by_id(client: TestClient, conditionnement_data):
    client.post(CONDIT_ENDPOINT, json=conditionnement_data)

    response: Response = client.get(f"{CONDIT_ENDPOINT}1")
    assert response.status_code == 200

    data = response.json()
    del data["id_condit"]

    expected = conditionnement_data.copy()

    assert data["lib_condit"] == expected["lib_condit"]
    assert data["poids_condit"] == expected["poids_condit"]
    assert data["ordre_imp"] == expected["ordre_imp"]
    assert norm_price(data["prix_condit"]) == norm_price(expected["prix_condit"])


def test_patch_conditionnement_by_id(client: TestClient, conditionnement_data):
    client.post(CONDIT_ENDPOINT, json=conditionnement_data)

    new_data = {
        "lib_condit": "Sachet 500g",
        "poids_condit": 500,
    }

    response: Response = client.patch(f"{CONDIT_ENDPOINT}1", json=new_data)
    assert response.status_code == 200
    assert response.json()["lib_condit"] == "Sachet 500g"
    assert response.json()["poids_condit"] == 500


def test_delete_conditionnement_by_id(client: TestClient, conditionnement_data):
    client.post(CONDIT_ENDPOINT, json=conditionnement_data)

    response: Response = client.delete(f"{CONDIT_ENDPOINT}1")
    assert response.status_code == 200

    response = client.get(f"{CONDIT_ENDPOINT}1")
    assert response.status_code == 404
    assert response.json().get("detail") == "Conditionnement non trouvé"
