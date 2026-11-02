from fastapi.testclient import TestClient


DETAILS = "/details-commandes"


def _create_client(client: TestClient, suffix: str = "1") -> int:
    commune = client.post(
        "/commune",
        json={"dep": "34", "cp": "34000", "ville": f"Details {suffix}"},
    )
    assert commune.status_code == 201, commune.text
    adresse = client.post(
        "/adresse",
        json={
            "rue": f"{suffix} rue des Details",
            "compAdresse": "",
            "id_commune": commune.json()["id_commune"],
        },
    )
    assert adresse.status_code == 201, adresse.text
    customer = client.post(
        "/clients",
        json={
            "email_client": f"details-{suffix}@example.com",
            "nom_client": "Details",
            "prenom_client": suffix,
            "adresse1_client": adresse.json()["id_adresse"],
        },
    )
    assert customer.status_code == 201, customer.text
    return customer.json()["id_client"]


def _create_commande(client: TestClient, suffix: str = "1", nb_colis=2) -> int:
    customer_id = _create_client(client, suffix)
    response = client.post(
        "/commandes",
        json={
            "date_commande": "2026-09-07",
            "id_client": customer_id,
            "nb_colis": nb_colis,
            "b_archive": False,
        },
    )
    assert response.status_code == 201, response.text
    return response.json()["id_commande"]


def _create_objet(
    client: TestClient,
    suffix: str = "1",
    indisponible: bool = False,
) -> int:
    response = client.post(
        "/objets",
        json={
            "nom_obj": f"Objet detail {suffix}",
            "prix_obj": 2.5,
            "poids_obj": 100,
            "indisp_obj": indisponible,
        },
    )
    assert response.status_code == 201, response.text
    return response.json()["id_objet"]


def _create_detail(
    client: TestClient,
    commande_id: int | None = None,
    objet_id: int | None = None,
    suffix: str = "1",
    **overrides,
):
    commande_id = commande_id or _create_commande(client, suffix)
    objet_id = objet_id or _create_objet(client, suffix)
    payload = {
        "quantite": 2,
        "commentaire": "Ligne MVP-02",
        "id_commande": commande_id,
        "id_objet": objet_id,
    }
    payload.update(overrides)
    response = client.post(DETAILS, json=payload)
    assert response.status_code == 201, response.text
    return response.json()


def test_create_read_and_list_by_commande_resets_nb_colis(client: TestClient):
    commande_id = _create_commande(client, nb_colis=2)
    objet_id = _create_objet(client)
    created = _create_detail(client, commande_id, objet_id)

    assert created["quantite"] == 2
    assert created["commentaire"] == "Ligne MVP-02"
    assert client.get(f"{DETAILS}/{created['id_detail_commande']}").json() == created

    listed = client.get(DETAILS, params={"commande_id": commande_id})
    assert listed.status_code == 200
    assert listed.json() == [created]
    assert client.get(f"/commandes/{commande_id}").json()["nb_colis"] is None


def test_rejects_invalid_quantity_and_unknown_references(client: TestClient):
    commande_id = _create_commande(client)
    objet_id = _create_objet(client)

    invalid_quantity = client.post(
        DETAILS,
        json={"quantite": 0, "id_commande": commande_id, "id_objet": objet_id},
    )
    assert invalid_quantity.status_code == 422

    unknown_commande = client.post(
        DETAILS,
        json={"quantite": 1, "id_commande": 9999, "id_objet": objet_id},
    )
    assert unknown_commande.status_code == 404

    unknown_objet = client.post(
        DETAILS,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": 9999},
    )
    assert unknown_objet.status_code == 404
    assert client.get(DETAILS, params={"commande_id": 9999}).status_code == 404


def test_rejects_duplicate_object_in_same_commande(client: TestClient):
    commande_id = _create_commande(client)
    objet_id = _create_objet(client)
    _create_detail(client, commande_id, objet_id)

    duplicate = client.post(
        DETAILS,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": objet_id},
    )
    assert duplicate.status_code == 409
    assert duplicate.json()["detail"] == "Cet objet est deja present dans la commande"


def test_patch_resets_nb_colis_and_allows_null_comment(client: TestClient):
    detail = _create_detail(client)
    commande_id = detail["id_commande"]
    assert client.patch(f"/commandes/{commande_id}", json={"nb_colis": 3}).status_code == 200

    response = client.patch(
        f"{DETAILS}/{detail['id_detail_commande']}",
        json={"quantite": 4, "commentaire": None},
    )
    assert response.status_code == 200, response.text
    assert response.json()["quantite"] == 4
    assert response.json()["commentaire"] is None
    assert client.get(f"/commandes/{commande_id}").json()["nb_colis"] is None


def test_delete_resets_nb_colis(client: TestClient):
    detail = _create_detail(client)
    commande_id = detail["id_commande"]
    assert client.patch(f"/commandes/{commande_id}", json={"nb_colis": 1}).status_code == 200

    response = client.delete(f"{DETAILS}/{detail['id_detail_commande']}")
    assert response.status_code == 200
    assert client.get(f"/commandes/{commande_id}").json()["nb_colis"] is None


def test_archived_commande_details_are_read_only(client: TestClient):
    detail = _create_detail(client)
    commande_id = detail["id_commande"]
    other_objet_id = _create_objet(client, "2")
    assert client.patch(f"/commandes/{commande_id}", json={"b_archive": True}).status_code == 200

    assert client.get(f"{DETAILS}/{detail['id_detail_commande']}").status_code == 200
    assert client.post(
        DETAILS,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": other_objet_id},
    ).status_code == 409
    assert client.patch(
        f"{DETAILS}/{detail['id_detail_commande']}",
        json={"quantite": 3},
    ).status_code == 409
    assert client.delete(f"{DETAILS}/{detail['id_detail_commande']}").status_code == 409


def test_commande_and_objet_with_detail_cannot_be_deleted(client: TestClient):
    detail = _create_detail(client)

    assert client.delete(f"/commandes/{detail['id_commande']}").status_code == 409
    objet_delete = client.delete(f"/objets/{detail['id_objet']}")
    assert objet_delete.status_code == 409
    assert objet_delete.json()["detail"] == "Objet utilise par une ligne de commande"


def test_unavailable_object_rules(client: TestClient):
    commande_id = _create_commande(client)
    unavailable_id = _create_objet(client, "indispo", indisponible=True)
    rejected = client.post(
        DETAILS,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": unavailable_id},
    )
    assert rejected.status_code == 409

    available_id = _create_objet(client, "available")
    detail = _create_detail(client, commande_id, available_id)
    assert client.patch(
        f"/objets/{available_id}",
        json={"indisp_obj": True},
    ).status_code == 200

    quantity_update = client.patch(
        f"{DETAILS}/{detail['id_detail_commande']}",
        json={"quantite": 5},
    )
    assert quantity_update.status_code == 200
    assert quantity_update.json()["quantite"] == 5

    switch_to_unavailable = client.patch(
        f"{DETAILS}/{detail['id_detail_commande']}",
        json={"id_objet": unavailable_id},
    )
    assert switch_to_unavailable.status_code == 409


def test_patch_rejects_duplicate_and_null_required_fields(client: TestClient):
    commande_id = _create_commande(client)
    first_objet = _create_objet(client, "first")
    second_objet = _create_objet(client, "second")
    first = _create_detail(client, commande_id, first_objet)
    second = _create_detail(client, commande_id, second_objet)

    duplicate = client.patch(
        f"{DETAILS}/{second['id_detail_commande']}",
        json={"id_objet": first_objet},
    )
    assert duplicate.status_code == 409

    for field in ("quantite", "id_objet"):
        response = client.patch(
            f"{DETAILS}/{first['id_detail_commande']}",
            json={field: None},
        )
        assert response.status_code == 422, (field, response.text)


def test_op_colis_can_read_objects_and_manage_details(client: TestClient, monkeypatch):
    commande_id = _create_commande(client)
    objet_id = _create_objet(client)
    role = client.post("/roles", json={"libelle_role": "OP-COLIS"})
    assert role.status_code == 201, role.text
    user = client.post(
        "/utilisateurs",
        json={
            "nom_user": "Operateur",
            "prenom_user": "Details",
            "username": "op.details",
            "password": "test-password",
            "id_role": role.json()["id_role"],
        },
    )
    assert user.status_code == 201, user.text
    headers = {"X-API-Key": user.json()["api_key"]}

    monkeypatch.setenv("DISABLE_AUTH", "false")
    assert client.get("/objets", headers=headers).status_code == 200
    created = client.post(
        DETAILS,
        headers=headers,
        json={"quantite": 1, "id_commande": commande_id, "id_objet": objet_id},
    )
    assert created.status_code == 201, created.text
    assert client.post(
        "/objets",
        headers=headers,
        json={"nom_obj": "Interdit"},
    ).status_code == 403
