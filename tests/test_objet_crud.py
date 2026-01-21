# tests/test_objet_crud.py

from fastapi import Response
from fastapi.testclient import TestClient
import pytest

# Constante endpoint (chez toi : /objets/ avec slash final)
OBJET_ENDPOINT = "/objets/"


@pytest.fixture
def objet_data():
    """Données de test pour créer un objet (schéma ObjetCreate)."""
    return {
        "nom_obj": "Objet pytest",
        "taille_obj": "M",
        "prix_obj": 1.25,
        "poids_obj": 0.50,
        "indisp_obj": False,
        "points_obj": 10,
    }


def test_get_all_objets(client: TestClient):
    """Tester l'obtention de tous les objets (doit renvoyer une liste vide au début)."""
    response: Response = client.get(OBJET_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_objet(client: TestClient, objet_data):
    """Tester la création d'un objet."""
    response: Response = client.post(OBJET_ENDPOINT, json=objet_data)
    assert response.status_code == 201

    data = response.json()

    # Champ auto-généré : on le retire avant comparaison
    assert "id_objet" in data
    del data["id_objet"]

    # Comparaison stricte : l'API renvoie exactement ce qu'on a envoyé
    assert data == objet_data


def test_get_objet_by_id(client: TestClient, objet_data):
    """Tester la récupération d'un objet par son ID."""

    # Créer un objet
    client.post(OBJET_ENDPOINT, json=objet_data)

    # Récupérer l'objet par ID (1er élément créé => id 1)
    response: Response = client.get(f"{OBJET_ENDPOINT}1")
    assert response.status_code == 200

    data = response.json()
    del data["id_objet"]
    assert data == objet_data


def test_patch_objet_by_id(client: TestClient, objet_data):
    """Tester la mise à jour partielle d'un objet."""

    # Créer un objet
    client.post(OBJET_ENDPOINT, json=objet_data)

    new_data = {
        "points_obj": 42,
        "indisp_obj": True,
        "nom_obj": "Objet modifié",
    }

    response: Response = client.patch(f"{OBJET_ENDPOINT}1", json=new_data)
    assert response.status_code == 200

    # Vérifie que les champs patchés ont changé
    assert response.json()["points_obj"] == 42
    assert response.json()["indisp_obj"] is True
    assert response.json()["nom_obj"] == "Objet modifié"


def test_delete_objet_by_id(client: TestClient, objet_data):
    """Tester la suppression d'un objet par son ID."""

    # Créer un objet
    client.post(OBJET_ENDPOINT, json=objet_data)

    # Supprimer l'objet
    response: Response = client.delete(f"{OBJET_ENDPOINT}1")
    assert response.status_code == 200  # OK

    # Vérifier que l'objet n'existe plus
    response: Response = client.get(f"{OBJET_ENDPOINT}1")
    assert response.status_code == 404  # Not Found
    assert response.json().get("detail") == "Objet non trouvé"
