# 🌟 Seja Bem-Vindo ao estudo de FASTAPI

## O que preisa ter
- Python 3.12

## Links importantes
https://fastapi.tiangolo.com/pt/virtual-environments/#verificando-um-ambiente-virtual

## Ambiente virtual

### Criação e ativação

```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate     # Windows
```

### Instalação

```bash
pip install -r requirements.txt
```

## Rotas

Rode com:
```bash
uvicorn app.main:app --reload
```

Documentação

```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

# Fazendo exemplo
# Criando POST e GET

controller/usuario_controller.py

```bash
def create_user(user):
    return user

def read_user():
    return {'name': 'seu_nome', 'age': 10, 'email': 'testes@teste.com'}
```

view/usuario_view.py

```bash
from http import HTTPStatus
from fastapi import APIRouter
from app.controllers.usuario_controller import create_user, read_user
from app.schemas.usuario_schema import User, UserPublic

router = APIRouter()

@router.post('/create_user', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def post_user(user: User):
    return create_user(user)

@router.get('/read_user')
def get_user():
    return read_user()
```
schemas/usuario_schema.py

```bash
from pydantic import BaseModel, EmailStr

class User (BaseModel):
    name: str
    age: int
    email: EmailStr
    password: str

class UserPublic (BaseModel):
    name: str
    age: int
    email: EmailStr
```

main.py

```bash
from app.views import testes_views, usuario_view

...

app.include_router(usuario_view.router, prefix="/users", tags=["Usuários"])
```

## Banco de dados

Crie um .env e adicione:

```bash
DATABASE_URL=sqlite:///./db.sqlite3
```

crie:

config.py

```bash
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
```

database/connection.py

```bash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
```

database/create_db.py

```bash
from app.database.connection import Base, engine

def create_tables():
    from app.models import usuario_model
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
```

Ajuste:

main.py

```bash
from app.database.create_db import create_tables

...

@app.on_event("startup")
def startup():
    create_tables()
```

Ajuste as tabelas:

models/usuario_model.py

```bash
from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
```

Verifique seu schema para ter os mesmos nomes de models:

schemas/usuario_schema.py

```bash
from pydantic import BaseModel, EmailStr
from typing import Optional

class User (BaseModel):
    name: str
    age: int
    email: EmailStr
    password: str

class UserPublic (BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]

class UsuarioOut(User):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
```

Faça as funções do endpoint:

controller/usuario_controller.py

```bash
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
```

Ajuste os endpoints:

view/usuario_view.py

```bash
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

```

## Alembic - pule
Iniciar Alembic:

```bash
alembic init alembic
```
Criar migração:

```bash
alembic revision --autogenerate -m "Criar tabela usuario"
```
Aplicar migração:

```bash
alembic upgrade head
```
