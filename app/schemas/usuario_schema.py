from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    senha: str
    nome: str
    telefone: str

class UserPublic(BaseModel):
    usuario_id: int
    nome: str
    telefone: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    nome: Optional[str]
    telefone: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]

