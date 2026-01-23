from typing import Callable

from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.utilisateur import Utilisateur
from ..repositories.utilisateur_repository import UtilisateurRepository

# ✅ Ceci fait apparaître le bouton "Authorize" dans Swagger
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def get_current_user_api_key(
    api_key: str | None = Depends(api_key_header),
    db: Session = Depends(get_db),
) -> Utilisateur:
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-API-Key manquante",
        )

    user = UtilisateurRepository.get_by_api_key(db, api_key)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-API-Key invalide",
        )
    return user


def require_roles(*allowed_roles: str) -> Callable:
    allowed = set(allowed_roles)

    def dependency(current_user: Utilisateur = Depends(get_current_user_api_key)) -> Utilisateur:
        # Chez vous : Role.libelle_role (vu dans role.py)
        role_name = None
        if getattr(current_user, "role", None) is not None:
            role_name = getattr(current_user.role, "libelle_role", None)

        if role_name not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Accès interdit",
            )
        return current_user

    return dependency
