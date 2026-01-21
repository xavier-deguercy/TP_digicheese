from fastapi import Response
from fastapi.testclient import TestClient
import pytest

# Constantes pour l'endpoint
ADRESSE_ENDPOINT = "/adresse"

@pytest.fixture
def adresse_data():
    """Données de test pour créer une adresse."""
    return {
        "rue": "Rue des Lila",
        "compAdresse": "RDC",
        "id_commune": 1
    }


def test_get_all_adresse(client: TestClient):
    """Tester l'obtention de tous les adresse (doit renvoyer une liste vide au début)."""
    response: Response = client.get(ADRESSE_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0

def test_create_adresse(client: TestClient, adresse_data):
    """Tester la création d'un adresse."""
    response: Response = client.post(ADRESSE_ENDPOINT, json=adresse_data)
    assert response.status_code == 201
    
    data = response.json()
    del data["id_adresse"]
    assert data == adresse_data  

def test_get_commune_by_id(client: TestClient,adresse_data):
    """Tester la récupération d'un adresse par son ID."""
    
    # Créer un adresse
    client.post(ADRESSE_ENDPOINT, json=adresse_data)
    
    # Récupérer le adresse par ID
    response: Response = client.get(f"{ADRESSE_ENDPOINT}/1")
    assert response.status_code == 200
    
    data = response.json()
    del data["id_adresse"]
    assert data == adresse_data  

def test_patch_adresse_by_id(client: TestClient, adresse_data  ):
    """Tester la mise à jour partielle des informations d'un adresse."""
    
    # Créer un adresse
    client.post(ADRESSE_ENDPOINT, json=adresse_data  )
    
    new_data = {
        "compAdresse": "première étage"
    }
    
    response: Response = client.patch(f"{ADRESSE_ENDPOINT}/1", json=new_data)
    assert response.status_code == 200
    assert response.json()["compAdresse"] == "première étage"


def test_delete_adresse_by_id(client: TestClient, adresse_data):
    """Tester la suppression d'un adresse par son ID."""

    # Créer un adresse
    client.post(ADRESSE_ENDPOINT, json=adresse_data)

    # Supprimer le adresse
    response: Response = client.delete(f"{ADRESSE_ENDPOINT}/1")
    assert response.status_code == 200  # OK

    # Vérifier que le adresse n'existe plus
    response: Response = client.get(f"{ADRESSE_ENDPOINT}/1")
    assert response.status_code == 404 # Not Found