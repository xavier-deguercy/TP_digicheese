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
        json={"dep": "34", "cp": "34000", "ville": f"MySQL MVP02 {stamp}"},
    )
    commune.raise_for_status()
    adresse = client.post(
        "/adresse",
        headers=headers,
        json={
            "rue": "2 rue MySQL",
            "compAdresse": "",
            "id_commune": commune.json()["id_commune"],
        },
    )
    adresse.raise_for_status()
    customer = client.post(
        "/clients",
        headers=headers,
        json={
            "email_client": f"mysql-mvp02-{stamp}@example.com",
            "nom_client": "MySQL",
            "prenom_client": "MVP02",
            "adresse1_client": adresse.json()["id_adresse"],
        },
    )
    customer.raise_for_status()
    available = client.post(
        "/objets",
        headers=headers,
        json={"nom_obj": f"Objet MVP02 {stamp}", "prix_obj": 2, "poids_obj": 100},
    )
    available.raise_for_status()
    unavailable = client.post(
        "/objets",
        headers=headers,
        json={
            "nom_obj": f"Objet indisponible MVP02 {stamp}",
            "prix_obj": 2,
            "poids_obj": 100,
            "indisp_obj": True,
        },
    )
    unavailable.raise_for_status()
    commande = client.post(
        "/commandes",
        headers=headers,
        json={
            "date_commande": "2026-09-07",
            "id_client": customer.json()["id_client"],
            "nb_colis": 2,
            "b_archive": False,
        },
    )
    commande.raise_for_status()

    commande_id = commande.json()["id_commande"]
    objet_id = available.json()["id_objet"]
    unavailable_id = unavailable.json()["id_objet"]
    created = client.post(
        "/details-commandes",
        headers=headers,
        json={
            "quantite": 2,
            "commentaire": "MySQL MVP-02",
            "id_commande": commande_id,
            "id_objet": objet_id,
        },
    )
    created.raise_for_status()
    detail_id = created.json()["id_detail_commande"]

    after_create = client.get(f"/commandes/{commande_id}", headers=headers)
    duplicate = client.post(
        "/details-commandes",
        headers=headers,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": objet_id},
    )
    unavailable_add = client.post(
        "/details-commandes",
        headers=headers,
        json={
            "quantite": 1,
            "id_commande": commande_id,
            "id_objet": unavailable_id,
        },
    )
    commande_delete_conflict = client.delete(
        f"/commandes/{commande_id}", headers=headers
    )
    objet_delete_conflict = client.delete(f"/objets/{objet_id}", headers=headers)
    archived = client.patch(
        f"/commandes/{commande_id}", headers=headers, json={"b_archive": True}
    )
    archived_edit = client.patch(
        f"/details-commandes/{detail_id}",
        headers=headers,
        json={"quantite": 3},
    )
    unarchived = client.patch(
        f"/commandes/{commande_id}", headers=headers, json={"b_archive": False}
    )
    updated = client.patch(
        f"/details-commandes/{detail_id}",
        headers=headers,
        json={"quantite": 3, "commentaire": None},
    )
    listed = client.get(
        "/details-commandes",
        headers=headers,
        params={"commande_id": commande_id},
    )
    deleted = client.delete(f"/details-commandes/{detail_id}", headers=headers)

    client.delete(f"/commandes/{commande_id}", headers=headers).raise_for_status()
    client.delete(f"/objets/{objet_id}", headers=headers).raise_for_status()
    client.delete(f"/objets/{unavailable_id}", headers=headers).raise_for_status()
    client.delete(
        f"/clients/{customer.json()['id_client']}", headers=headers
    ).raise_for_status()
    client.delete(
        f"/adresse/{adresse.json()['id_adresse']}", headers=headers
    ).raise_for_status()
    client.delete(
        f"/commune/{commune.json()['id_commune']}", headers=headers
    ).raise_for_status()

result = {
    "database": "MySQL Docker",
    "authentication": "Admin X-API-Key",
    "create_detail": created.status_code,
    "nb_colis_after_create": after_create.json()["nb_colis"],
    "duplicate": duplicate.status_code,
    "unavailable_object": unavailable_add.status_code,
    "commande_delete_with_detail": commande_delete_conflict.status_code,
    "objet_delete_with_detail": objet_delete_conflict.status_code,
    "archive": archived.status_code,
    "archived_detail_edit": archived_edit.status_code,
    "unarchive": unarchived.status_code,
    "update_detail": updated.status_code,
    "list_by_commande": listed.status_code,
    "delete_detail": deleted.status_code,
    "cleanup": "complete",
}
print(json.dumps(result, ensure_ascii=False, indent=2))
