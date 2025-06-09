from pydantic import BaseModel
from app.config import settings

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm


class Token(BaseModel):
    pass


class RefreshToken(BaseModel):
    pass


class TokenData(BaseModel):
    pass



