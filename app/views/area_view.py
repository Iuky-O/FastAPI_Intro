from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.area_schema import AreaCreate, AreaUpdate, AreaPublic
from http import HTTPStatus
from typing import List

from app.controllers.area_controller import (
    criar_area,
    listar_areas,
    alterar_area,
    apagar_area,
    listar_area_id,
    buscar_area_status
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AreaPublic, status_code=HTTPStatus.CREATED)
def criar(area: AreaCreate, db: Session = Depends(get_db)):
    return criar_area(db, area)

@router.get("/", response_model=list[AreaPublic])
def listar(db: Session = Depends(get_db)):
    return listar_areas(db)

@router.get("/{area_id}", response_model=AreaPublic)
def listar_por_id(area_id: int, db: Session = Depends(get_db)):
    return listar_area_id(db, area_id)

@router.put("/{area_id}", response_model=AreaPublic)
def alterar(area_id: int, area: AreaUpdate, db: Session = Depends(get_db)):
    return alterar_area(db, area_id, area)

@router.delete("/{area_id}", status_code=204)
def apagar(area_id: int, db: Session = Depends(get_db)):
    apagar_area(db, area_id)
    return None

@router.get("/status/{area_status}", response_model=List[AreaPublic])
def buscar_por_status(area_status: str, db: Session = Depends(get_db)):
    return buscar_area_status(db, area_status)
