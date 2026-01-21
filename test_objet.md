B) Objets
1) GET /objets/

Attendu : 200 + [] ou liste
reponse 200 avec liste vide au debut

2) POST /objets/

Ton modèle impose généralement nom_obj (NOT NULL). Payload minimal + cohérent :

{
  "nom_obj": "Couteau à fromage",
  "taille_obj": "M",
  "prix_obj": "9.99",
  "poids_obj": "0.12",
  "indisp_obj": false,
  "points_obj": 100
}


Attendu : 201 + id_obj (ou équivalent) + valeurs.
reponse 201 avec id_obj et valeurs renvoyées
{
  "id_objet": 1,
  "nom_obj": "Couteau à fromage",
  "taille_obj": "M",
  "prix_obj": 9.99,
  "poids_obj": 0.12,
  "indisp_obj": false,
  "points_obj": 100
}


3) PATCH /objets/{objet_id}

Exemple :

{
  "indisp_obj": true
}


Attendu : 200

reponse 
Code	Details
200	 Response body


{
  "id_objet": 1,
  "nom_obj": "Couteau à fromage",
  "taille_obj": "M",
  "prix_obj": 9.99,
  "poids_obj": 0.12,
  "indisp_obj": true,
  "points_obj": 100
}

4) DELETE /objets/{objet_id}

Attendu : 200

Code	Details
200	
Response body
Download
{
  "id_objet": 1,
  "nom_obj": "Couteau à fromage",
  "taille_obj": "M",
  "prix_obj": 9.99,
  "poids_obj": 0.12,
  "indisp_obj": true,
  "points_obj": 100
}


