from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from app.schemas.usuario_schema import UserPublic
from app.config import settings

security = HTTPBearer()
SECRET_KEY = settings.security.SECRET_KEY
ALGORITHM = settings.security.ALGORITHM

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> UserPublic:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: int = payload.get("user_id")
        nome: str = payload.get("nome")
        telefone: str = payload.get("telefone")
        email: str = payload.get("email")

        if usuario_id is None or email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
            )

        return UserPublic(
            usuario_id=usuario_id,
            nome=nome,
            telefone=telefone,
            email=email,
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )
