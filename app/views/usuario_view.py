#Aqui fica as view (rotas) do user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.usuario_schema import UsuarioOut, UserPublic, UserUpdate, User
from http import HTTPStatus

from app.controllers.usuario_controller import (
        criar_usuario,
        listar_usuarios,
        alterar_usuario,
        apagar_usuario,
        listar_usuarios_id
    )

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut, status_code=HTTPStatus.CREATED)
def criar(usuario: User, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)

@router.get("/{user_id}", response_model=UserPublic)
def listar_por_id(user_id: int, db: Session = Depends(get_db)):
    return listar_usuarios_id(db, user_id)

@router.put("/{user_id}", response_model=UserPublic)
def alterar(user_id: int, usuario: User, db: Session = Depends(get_db)):
    return alterar_usuario(db, user_id, usuario)

@router.delete("/{user_id}", status_code=204)
def apagar(user_id: int, db: Session = Depends(get_db)):
    apagar_usuario(db, user_id)
    return None