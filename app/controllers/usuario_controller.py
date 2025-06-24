from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import User, UserUpdate
from fastapi import HTTPException
from app.services.auth_service import gerar_hash_senha 

def criar_usuario(db: Session, usuario: User):
    senha_hash = gerar_hash_senha(usuario.senha)

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        telefone=usuario.telefone,
        senha=senha_hash,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def listar_usuarios_id(db: Session, user_id: int):
    usuario = db.query(Usuario).filter(Usuario.usuario_id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

def alterar_usuario(db: Session, user_id: int, dados: UserUpdate):
    usuario = db.query(Usuario).filter(Usuario.usuario_id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    for key, value in dados.dict(exclude_unset=True).items():
        if key == "senha" and value:
            value = gerar_hash_senha(value)
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario

def apagar_usuario(db: Session, user_id: int):
    usuario = db.query(Usuario).filter(Usuario.usuario_id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    db.delete(usuario)
    db.commit()
