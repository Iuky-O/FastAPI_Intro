from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.exame_imagem_schema import ExameImagemPublic, ExameImagemBase, ExameImagemUpdate
from http import HTTPStatus
from app.database.connection import get_db

from app.controllers.imagem_exame_controller import (
        criar_exames_imagem, listar_exames_imagem, listar_exames_imagem_id,
        alterar_exame_imagem, apagar_exame_imagem
    )

router = APIRouter()


@router.post("/", response_model=ExameImagemPublic, status_code=HTTPStatus.CREATED)
def criar(exame_imagem: ExameImagemBase, db: Session = Depends(get_db)):
    return criar_exames_imagem(db, exame_imagem)

@router.get("/", response_model=list[ExameImagemPublic])
def listar(db: Session = Depends(get_db)):
    return listar_exames_imagem(db)

@router.get("/{exame_id}", response_model=ExameImagemPublic)
def listar_por_id(exame_id: int, db: Session = Depends(get_db)):
    return listar_exames_imagem_id(db, exame_id)

@router.put("/{img_exame_id}", response_model=ExameImagemPublic)
def alterar(img_exame_id: int, exame_imagem: ExameImagemUpdate, db: Session = Depends(get_db)):
    return alterar_exame_imagem(db, img_exame_id, exame_imagem)

@router.delete("/{img_exame_id}", status_code=204)
def apagar(img_exame_id: int, db: Session = Depends(get_db)):
    apagar_exame_imagem(db, img_exame_id)
    return None