from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.usuario_schema import UserPublic

class SecretariaBase(BaseModel):
    nome: str
    cpf: str
    rg: str
    usuario_id: int

class SecretariaCreate(SecretariaBase):
    pass

class SecretariaPublic(BaseModel):
    secretaria_id: int
    nome: str
    cpf: str
    rg: str
    usuario: UserPublic

    class Config:
        orm_mode = True

class SecretariaUpdate(BaseModel):
    nome: Optional[str]

class SecretariaGet(BaseModel):
    secretaria_id: int
    nome: str
    cpf: str
    rg: str
    usuario_id: int

    class Config:
        orm_mode = True
