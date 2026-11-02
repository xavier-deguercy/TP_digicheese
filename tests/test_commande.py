from fastapi.testclient import TestClient


COMMANDES = "/commandes"


def _create_client(client: TestClient, suffix: str = "1") -> int:
    commune = client.post(
        "/commune",
        json={"dep": "34", "cp": "34000", "ville": f"Montpellier {suffix}"},
    )
    assert commune.status_code == 201, commune.text
    adresse = client.post(
        "/adresse",
        json={
            "rue": f"{suffix} rue des Commandes",
            "compAdresse": "",
            "id_commune": commune.json()["id_commune"],
        },
    )
    assert adresse.status_code == 201, adresse.text
    response = client.post(
        "/clients",
        json={
            "email_client": f"commande-{suffix}@example.com",
            "nom_client": "Client",
            "prenom_client": suffix,
            "adresse1_client": adresse.json()["id_adresse"],
        },
    )
    assert response.status_code == 201, response.text
    return response.json()["id_client"]


def _create_conditionnement(client: TestClient, suffix: str = "1") -> int:
    response = client.post(
        "/conditionnements",
        json={"lib_condit": f"Carton {suffix}", "poids_condit": 250, "prix_condit": 1},
    )
    assert response.status_code == 201, response.text
    return response.json()["id_condit"]


def _commande_payload(id_client: int, **overrides):
    payload = {
        "date_commande": "2026-09-07",
        "id_client": id_client,
        "id_conditionnement": None,
        "nb_colis": None,
        "b_archive": False,
    }
    payload.update(overrides)
    return payload


def _create_commande(client: TestClient, **overrides):
    id_client = _create_client(client)
    response = client.post(COMMANDES, json=_commande_payload(id_client, **overrides))
    assert response.status_code == 201, response.text
    return response.json()


def test_create_and_read_commande_without_conditionnement(client: TestClient):
    created = _create_commande(client)

    assert created["id_conditionnement"] is None
    assert created["nb_colis"] is None
    assert created["b_archive"] is False

    response = client.get(f"{COMMANDES}/{created['id_commande']}")
    assert response.status_code == 200
    assert response.json() == created


def test_list_commandes(client: TestClient):
    first = _create_commande(client)
    response = client.get(COMMANDES)

    assert response.status_code == 200
    assert [item["id_commande"] for item in response.json()] == [first["id_commande"]]


def test_rejects_unknown_client_and_conditionnement(client: TestClient):
    response = client.post(COMMANDES, json=_commande_payload(9999))
    assert response.status_code == 400
    assert response.json()["detail"] == "id_client: client inconnu"

    id_client = _create_client(client)
    response = client.post(
        COMMANDES,
        json=_commande_payload(id_client, id_conditionnement=9999),
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "id_conditionnement: conditionnement inconnu"


def test_nb_colis_must_be_positive_when_present(client: TestClient):
    id_client = _create_client(client)
    response = client.post(COMMANDES, json=_commande_payload(id_client, nb_colis=0))
    assert response.status_code == 422


def test_changing_conditionnement_clears_nb_colis(client: TestClient):
    id_conditionnement = _create_conditionnement(client)
    created = _create_commande(
        client,
        id_conditionnement=id_conditionnement,
        nb_colis=2,
    )

    response = client.patch(
        f"{COMMANDES}/{created['id_commande']}",
        json={"id_conditionnement": None, "nb_colis": 3},
    )

    assert response.status_code == 200, response.text
    assert response.json()["id_conditionnement"] is None
    assert response.json()["nb_colis"] is None


def test_archived_commande_is_locked_until_unarchived(client: TestClient):
    created = _create_commande(client)
    endpoint = f"{COMMANDES}/{created['id_commande']}"

    archived = client.patch(endpoint, json={"b_archive": True})
    assert archived.status_code == 200
    assert archived.json()["b_archive"] is True

    blocked = client.patch(endpoint, json={"nb_colis": 1})
    assert blocked.status_code == 409

    unarchived = client.patch(endpoint, json={"b_archive": False})
    assert unarchived.status_code == 200
    assert unarchived.json()["b_archive"] is False

    modified = client.patch(endpoint, json={"nb_colis": 1})
    assert modified.status_code == 200
    assert modified.json()["nb_colis"] == 1


def test_archiving_incomplete_commande_is_allowed(client: TestClient):
    created = _create_commande(client)
    response = client.patch(
        f"{COMMANDES}/{created['id_commande']}",
        json={"b_archive": True},
    )

    assert response.status_code == 200
    assert response.json()["b_archive"] is True
    assert response.json()["id_conditionnement"] is None
    assert response.json()["nb_colis"] is None


def test_delete_only_non_archived_commande(client: TestClient):
    created = _create_commande(client)
    endpoint = f"{COMMANDES}/{created['id_commande']}"

    assert client.patch(endpoint, json={"b_archive": True}).status_code == 200
    assert client.delete(endpoint).status_code == 409
    assert client.patch(endpoint, json={"b_archive": False}).status_code == 200
    assert client.delete(endpoint).status_code == 200
    assert client.get(endpoint).status_code == 404


def test_referenced_client_and_conditionnement_cannot_be_deleted(client: TestClient):
    id_client = _create_client(client)
    id_conditionnement = _create_conditionnement(client)
    created = client.post(
        COMMANDES,
        json=_commande_payload(
            id_client,
            id_conditionnement=id_conditionnement,
            nb_colis=1,
        ),
    )
    assert created.status_code == 201, created.text

    client_delete = client.delete(f"/clients/{id_client}")
    assert client_delete.status_code == 409
    assert client_delete.json()["detail"] == "Client utilise par une commande"

    conditionnement_delete = client.delete(
        f"/conditionnements/{id_conditionnement}"
    )
    assert conditionnement_delete.status_code == 409
    assert conditionnement_delete.json()["detail"] == (
        "Conditionnement utilise par une commande"
    )


def test_patch_rejects_null_required_fields(client: TestClient):
    created = _create_commande(client)
    endpoint = f"{COMMANDES}/{created['id_commande']}"

    for field in ("date_commande", "id_client", "b_archive"):
        response = client.patch(endpoint, json={field: None})
        assert response.status_code == 422, (field, response.text)


def test_op_colis_can_access_commandes(client: TestClient, monkeypatch):
    created = _create_commande(client)
    role = client.post("/roles", json={"libelle_role": "OP-COLIS"})
    assert role.status_code == 201, role.text
    user = client.post(
        "/utilisateurs",
        json={
            "nom_user": "Operateur",
            "prenom_user": "Commandes",
            "username": "op.commandes",
            "password": "test-password",
            "id_role": role.json()["id_role"],
        },
    )
    assert user.status_code == 201, user.text

    monkeypatch.setenv("DISABLE_AUTH", "false")
    response = client.get(
        f"{COMMANDES}/{created['id_commande']}",
        headers={"X-API-Key": user.json()["api_key"]},
    )

    assert response.status_code == 200, response.text
