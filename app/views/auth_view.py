from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.auth_service import verificar_senha, criar_acesso_token
from app.models.usuario_model import Usuario
from datetime import timedelta

router = APIRouter()

@router.post("/token")
def login(
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if not usuario or not verificar_senha(senha, usuario.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )

    access_token_expires = timedelta(minutes=30)
    token = criar_acesso_token(
        data={
            "user_id": usuario.usuario_id,
            "email": usuario.email,
            "nome": usuario.nome,
            "telefone": usuario.telefone,
        },
        expires_delta=access_token_expires,
    )

    return {"access_token": token, "token_type": "bearer"}
