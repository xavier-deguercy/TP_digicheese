"""Charge l'ensemble des modèles afin de résoudre les relations SQLAlchemy."""

from .adresse import Adresse
from .client import Client
from .commune import Commune
from .commande import Commande
from .conditionnement import Conditionnement
from .detail_commande import DetailCommande
from .objet import Objet
from .poids import Poids
from .poidsv import Poidsv
from .role import Role
from .utilisateur import Utilisateur

__all__ = [
    "Adresse",
    "Client",
    "Commune",
    "Commande",
    "Conditionnement",
    "DetailCommande",
    "Objet",
    "Poids",
    "Poidsv",
    "Role",
    "Utilisateur",
]
