from pydantic import BaseModel, EmailStr
from typing import Optional


class Pacient(BaseModel):
    """ Schema Pacient Padrão"""
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    data_cadastro: str
    endereco: str
    telefone: str
    email: EmailStr
    plano_saude: bool


class PacientPublic(BaseModel):
    """(Classe Pública para mudança?)"""
    paciente_id: int
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    data_cadastro: str
    endereco: str
    telefone: str
    email: EmailStr
    plano_saude: bool

    class Config:
        """ orm_mode mudou para from_atributes
         * UserWarning: Valid config keys have changed in V2: *
         * 'orm_mode' has been renamed to 'from_attributes'   *
        """
        from_attributes = True


class PacientUpdate(BaseModel):
    """ Classe Pacient Atualizável"""
    nome: Optional[str]
    data_nascimento: Optional[str]
    rg: Optional[str]
    cpf: Optional[str]
    data_cadastro: Optional[str]
    endereco: Optional[str]
    telefone: Optional[str]
    email: Optional[EmailStr]
    plano_saude: Optional[bool]


class PacientOut(PacientPublic):
    """ Classe Pacient Out """
    pass
