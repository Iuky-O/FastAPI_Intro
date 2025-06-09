from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.usuario_schema import UserPublic
from app.schemas.area_schema import AreaPublic

class MedicoBase(BaseModel):
    nome: str
    cpf: str
    rg: str
    crm_numero: str
    crm_UF: str
    usuario_id: int
    area_id: int

class MedicoCreate(MedicoBase):
    pass

class MedicoPublic(BaseModel):
    medico_id: int
    nome: str
    cpf: str
    rg: str
    crm_numero: str
    crm_UF: str
    usuario: UserPublic
    area: AreaPublic

    class Config:
        orm_mode = True

class MedicoUpdate(BaseModel):
    nome: Optional[str]
    area_id: Optional[int]

class MedicoGet(BaseModel):
    medico_id: int
    nome: str
    cpf: str
    rg: str
    crm_numero: str
    crm_UF: str
    usuario_id: int
    area_id: int

    class Config:
        orm_mode = True
