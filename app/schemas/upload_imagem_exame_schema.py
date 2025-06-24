from pydantic import BaseModel, validator, Field
from typing import Optional
from app.schemas.exame_imagem_schema import ExameImagemPublic

class UploadExameImagemBase(BaseModel):
    titulo: str = Field(..., min_length=1)
    upload: str
    exame_imagem_id: int

    @validator("titulo", "upload")
    def nao_pode_ser_vazio(cls, v):
        if not v.strip():
            raise ValueError("Campo obrigatório e não pode ser vazio")
        return v

class UploadExameImagemCreate(UploadExameImagemBase):
    pass

class UploadExameImagemUpdate(BaseModel):
    titulo: Optional[str]
    upload: Optional[str]
    exame_imagem_id: Optional[int]

class UploadExameImagemPublic(UploadExameImagemBase):
    upload_id: int

    class Config:
        orm_mode = True
