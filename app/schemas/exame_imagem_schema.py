from pydantic import BaseModel
from typing import Optional

class ExameImagemBase(BaseModel):
    tipo: str
    descricao: Optional[str]
    link_imagem: Optional[str] = None

class ExameImagemPublic(ExameImagemBase):
    exame_id: int

    class Config:
        orm_mode = True

class ExameImagemUpdate(BaseModel):
    tipo: Optional[str]
    descricao: Optional[str]
    link_imagem: Optional[str]
