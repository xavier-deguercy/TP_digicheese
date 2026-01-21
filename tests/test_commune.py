from fastapi import Response
from fastapi.testclient import TestClient
import pytest

# Constantes pour l'endpoint
COMMUNE_ENDPOINT = "/commune"

@pytest.fixture
def commune_data():
    """Données de test pour créer une commune."""
    return {
        "dep": "Haute-Garonne",
        "cp": "31000",
        "ville": "Toulouse"
    }


def test_get_all_commune(client: TestClient):
    """Tester l'obtention de tous les communes (doit renvoyer une liste vide au début)."""
    response: Response = client.get(COMMUNE_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0

def test_create_commune(client: TestClient, commune_data):
    """Tester la création d'un commune."""
    response: Response = client.post(COMMUNE_ENDPOINT, json=commune_data)
    assert response.status_code == 201
    
    data = response.json()
    del data["id_commune"]
    assert data == commune_data  

def test_get_commune_by_id(client: TestClient,commune_data):
    """Tester la récupération d'un commune par son ID."""
    
    # Créer un commune
    client.post(COMMUNE_ENDPOINT, json=commune_data)
    
    # Récupérer le commune par ID
    response: Response = client.get(f"{COMMUNE_ENDPOINT}/1")
    assert response.status_code == 200
    
    data = response.json()
    del data["id_commune"]
    assert data == commune_data  

def test_patch_commune_by_id(client: TestClient, commune_data):
    """Tester la mise à jour partielle des informations d'un commune."""
    
    # Créer un commune
    client.post(COMMUNE_ENDPOINT, json=commune_data)
    
    new_data = {
        "ville": "Colomier"
    }
    
    response: Response = client.patch(f"{COMMUNE_ENDPOINT}/1", json=new_data)
    assert response.status_code == 200
    assert response.json()["ville"] == "Colomier"

def test_delete_commune_by_id(client: TestClient, commune_data):
    """Tester la suppression d'un commune par son ID."""

    # Créer un commune
    client.post(COMMUNE_ENDPOINT, json=commune_data)

    # Supprimer le commune
    response: Response = client.delete(f"{COMMUNE_ENDPOINT}/1")
    assert response.status_code == 200  # OK

    # Vérifier que le commune n'existe plus
    response: Response = client.get(f"{COMMUNE_ENDPOINT}/1")
    assert response.status_code == 404 # Not Found