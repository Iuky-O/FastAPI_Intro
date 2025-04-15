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

## Alembic
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

Documentação
```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
