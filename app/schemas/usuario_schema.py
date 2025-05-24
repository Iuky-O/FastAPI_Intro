# #Aqui fica o schema do user (entrada e saida de dados)
# from pydantic import BaseModel, EmailStr
# from typing import Optional

# class User (BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#     password: str

# class UserPublic (BaseModel):
#     id: int
#     name: str
#     age: int
#     email: EmailStr

# class UserUpdate(BaseModel):
#     name: Optional[str]
#     age: Optional[int]
#     email: Optional[EmailStr]

# class UsuarioOut(User):
#     id: int
#     name: str
#     email: EmailStr

#     class Config:
#         orm_mode = True

from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    senha: str
    nome: str
    telefone: str

class UserPublic(BaseModel):
    id_usuario: int
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

class UsuarioOut(UserPublic):
    pass
