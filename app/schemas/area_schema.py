from pydantic import BaseModel
from typing import Optional

class AreaBase(BaseModel):
    titulo: str
    status: str

class AreaCreate(AreaBase):
    pass

class AreaUpdate(BaseModel):
    titulo: Optional[str]
    status: Optional[str]

class AreaPublic(AreaBase):
    area_id: int

    class Config:
        orm_mode = True
