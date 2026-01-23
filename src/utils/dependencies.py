from typing import Callable
import os
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.utilisateur import Utilisateur
from ..repositories.utilisateur_repository import UtilisateurRepository

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def get_current_user_api_key(
    api_key: str | None = Depends(api_key_header),
    db: Session = Depends(get_db),
) -> Optional[Utilisateur]:

    if os.getenv("DISABLE_AUTH", "false").lower() == "true":
        return None

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


def require_roles(*allowed_roles: str):
    def dependency(current_user=Depends(get_current_user_api_key)):
        if os.getenv("DISABLE_AUTH", "false").lower() == "true":
            return current_user  # ou même return None si tu préfères

        role_name = current_user.role.libelle_role
        if role_name not in allowed_roles:
            raise HTTPException(status_code=403, detail="Accès interdit")
        return current_user
    return dependency
