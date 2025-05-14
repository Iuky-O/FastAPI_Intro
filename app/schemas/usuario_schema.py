#Aqui fica o schema do user (entrada e saida de dados)
from pydantic import BaseModel, EmailStr
from typing import Optional

class User (BaseModel):
    name: str
    age: int
    email: EmailStr
    password: str

class UserPublic (BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]

class UsuarioOut(User):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True