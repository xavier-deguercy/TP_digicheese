POST /conditionnements/

{
  "lib_condit": "Sachet 250g",
  "poids_condit": 250,
  "prix_condit": "0",
  "ordre_imp": 1
}

Code 201
{
  "lib_condit": "Sachet 250g",
  "poids_condit": 250,
  "prix_condit": "0.0000",
  "ordre_imp": 1,
  "id_condit": 1
}
3) GET /conditionnements/{condit_id}

Mets l’ID retourné

Attendu : 200 + l’objet

ok 200
{
  "lib_condit": "Sachet 250g",
  "poids_condit": 250,
  "prix_condit": "0.0000",
  "ordre_imp": 1,
  "id_condit": 1
}

4) PATCH /conditionnements/{condit_id}

Exemple (modif partielle) :

{
  "prix_condit": "0.20",
  "ordre_imp": 2
}

200	
Response body
Download
{
  "lib_condit": "Sachet 250g",
  "poids_condit": 250,
  "prix_condit": "0.2000",
  "ordre_imp": 2,
  "id_condit": 1
}

5) DELETE /conditionnements/{condit_id}

Attendu : 200 + objet supprimé (si tu renvoies l’objet supprimé)
reponse 200 et objet suprimé dans mysql
6) GET /conditionnements/{condit_id} (après delete)

Attendu : 404
retour 404 not found