from sqlalchemy.orm import Session
from app.models.area_model import Area
from app.schemas.area_schema import AreaCreate, AreaUpdate
from fastapi import HTTPException
from app.utils.validar_status_area import validar_status

def criar_area(db: Session, area: AreaCreate):
    validar_status(area.status)
    nova_area = Area(**area.dict())
    db.add(nova_area)
    db.commit()
    db.refresh(nova_area)
    return nova_area

def listar_areas(db: Session):
    return db.query(Area).all()

def listar_area_id(db: Session, area_id: int):
    area = db.query(Area).filter(Area.area_id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área não encontrada")
    return area

def alterar_area(db: Session, area_id: int, dados: AreaUpdate):
    area = db.query(Area).filter(Area.area_id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área não encontrada")
    
    update_data = dados.dict(exclude_unset=True)

    if "status" in update_data:
        validar_status(update_data["status"])

    for key, value in dados.dict(exclude_unset=True).items():
        setattr(area, key, value)

    db.commit()
    db.refresh(area)
    return area

def apagar_area(db: Session, area_id: int):
    area = db.query(Area).filter(Area.area_id == area_id).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área não encontrada")
    
    db.delete(area)
    db.commit()

def buscar_area_status(db: Session, status: str):
    validar_status(status)
    return db.query(Area).filter(Area.status == status).all()
