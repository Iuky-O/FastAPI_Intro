#Aqui fica o controller do user (funções das rotas - views)
from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import User
from fastapi import APIRouter, Depends, HTTPException

def criar_usuario(db: Session, usuario: User):
    novo_usuario = Usuario(**usuario.dict())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def listar_usuarios_id(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

def alterar_usuario(db: Session, user_id: int, dados: User):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    for key, value in dados.dict().items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario

def apagar_usuario(db: Session, user_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    db.delete(usuario)
    db.commit()