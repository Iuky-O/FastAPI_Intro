#Aqui fica as view (rotas) do user


from http import HTTPStatus
from fastapi import Path
from fastapi import APIRouter
# from app.controllers.usuario_controller import create_user, read_user, delete_user, update_user
from app.schemas.usuario_schema import User, UserPublic, UserUpdate

router = APIRouter()

# @router.post('/create_user', status_code=HTTPStatus.CREATED, response_model=UserPublic)
# def post_user(user: User):
#     return create_user(user)

# @router.get('/read_user')
# def get_user():
#     return read_user()

# @router.put('/update_user/{user_id}')
# def put_user(user_id: int = Path(...), user: User = None):
#     return update_user(user_id, user)

# @router.delete('/delete_user/{user_id}', status_code=HTTPStatus.NO_CONTENT)
# def delete_user_route(user_id: int = Path(...)):
#     return delete_user(user_id)


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.usuario_schema import UsuarioOut
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
def listar(user_id: int, db: Session = Depends(get_db)):
    return listar_usuarios_id(db, user_id)

@router.put("/{user_id}", response_model=UserPublic)
def alterar(user_id: int, usuario: User, db: Session = Depends(get_db)):
    return alterar_usuario(db, user_id, usuario)

@router.delete("/{user_id}", status_code=204)
def apagar(user_id: int, db: Session = Depends(get_db)):
    apagar_usuario(db, user_id)
    return None


