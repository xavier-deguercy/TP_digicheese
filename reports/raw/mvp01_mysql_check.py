import json
import os
import time

from fastapi.testclient import TestClient
from sqlalchemy import select

os.environ["DISABLE_AUTH"] = "false"

from src.database import SessionLocal  # noqa: E402
from src.main import app  # noqa: E402
from src.models.role import Role  # noqa: E402
from src.models.utilisateur import Utilisateur  # noqa: E402


with SessionLocal() as db:
    api_key = db.scalar(
        select(Utilisateur.api_key)
        .join(Role, Role.id_role == Utilisateur.id_role)
        .where(Role.libelle_role == "Admin", Utilisateur.api_key.is_not(None))
        .limit(1)
    )

if not api_key:
    raise RuntimeError("Aucune cle Admin disponible pour le controle MySQL")

headers = {"X-API-Key": api_key}
stamp = int(time.time() * 1000)

with TestClient(app) as client:
    commune = client.post(
        "/commune",
        headers=headers,
        json={"dep": "34", "cp": "34000", "ville": f"MySQL MVP01 {stamp}"},
    )
    commune.raise_for_status()
    adresse = client.post(
        "/adresse",
        headers=headers,
        json={
            "rue": "1 rue MySQL",
            "compAdresse": "",
            "id_commune": commune.json()["id_commune"],
        },
    )
    adresse.raise_for_status()
    customer = client.post(
        "/clients",
        headers=headers,
        json={
            "email_client": f"mysql-mvp01-{stamp}@example.com",
            "nom_client": "MySQL",
            "prenom_client": "MVP01",
            "adresse1_client": adresse.json()["id_adresse"],
        },
    )
    customer.raise_for_status()
    packaging = client.post(
        "/conditionnements",
        headers=headers,
        json={
            "lib_condit": f"MySQL MVP01 {stamp}",
            "poids_condit": 250,
            "prix_condit": 1,
        },
    )
    packaging.raise_for_status()

    customer_id = customer.json()["id_client"]
    packaging_id = packaging.json()["id_condit"]
    created = client.post(
        "/commandes",
        headers=headers,
        json={
            "date_commande": "2026-09-07",
            "id_client": customer_id,
            "id_conditionnement": packaging_id,
            "nb_colis": 2,
            "b_archive": False,
        },
    )
    created.raise_for_status()
    command_id = created.json()["id_commande"]

    customer_delete_conflict = client.delete(
        f"/clients/{customer_id}", headers=headers
    )
    packaging_delete_conflict = client.delete(
        f"/conditionnements/{packaging_id}", headers=headers
    )
    archived = client.patch(
        f"/commandes/{command_id}", headers=headers, json={"b_archive": True}
    )
    locked = client.patch(
        f"/commandes/{command_id}", headers=headers, json={"nb_colis": 1}
    )
    unarchived = client.patch(
        f"/commandes/{command_id}", headers=headers, json={"b_archive": False}
    )
    changed = client.patch(
        f"/commandes/{command_id}",
        headers=headers,
        json={"id_conditionnement": None, "nb_colis": 3},
    )
    listed = client.get("/commandes", headers=headers)
    deleted = client.delete(f"/commandes/{command_id}", headers=headers)

    client.delete(f"/conditionnements/{packaging_id}", headers=headers).raise_for_status()
    client.delete(f"/clients/{customer_id}", headers=headers).raise_for_status()
    client.delete(f"/adresse/{adresse.json()['id_adresse']}", headers=headers).raise_for_status()
    client.delete(f"/commune/{commune.json()['id_commune']}", headers=headers).raise_for_status()

result = {
    "database": "MySQL Docker",
    "authentication": "Admin X-API-Key",
    "create": created.status_code,
    "referenced_client_delete": customer_delete_conflict.status_code,
    "referenced_conditionnement_delete": packaging_delete_conflict.status_code,
    "archive": archived.status_code,
    "archived_edit": locked.status_code,
    "unarchive": unarchived.status_code,
    "conditionnement_change": changed.status_code,
    "nb_colis_after_conditionnement_change": changed.json()["nb_colis"],
    "list": listed.status_code,
    "delete": deleted.status_code,
    "cleanup": "complete",
}
print(json.dumps(result, ensure_ascii=False, indent=2))
