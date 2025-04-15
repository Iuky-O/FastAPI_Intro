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

```bash

```
