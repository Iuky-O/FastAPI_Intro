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
    return {'nome': 'Iumy', 'idade': 22, 'email': 'teste@teste.com'}
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

### Criando PUT e DELETE

## Banco de dados

Crie um .env e adicione:

```bash
DATABASE_URL=sqlite:///./db.sqlite3
```
