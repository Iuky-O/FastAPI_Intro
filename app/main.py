from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from http import HTTPStatus
# from app.database.connection import create_tables
from app.views import testes_views, usuario_view

app = FastAPI()

# @app.on_event("startup")
# def startup():
#     create_tables()

app.include_router(testes_views.router, prefix="/testes", tags=["Testes"])
# app.include_router(usuario_view.router, prefix="/users", tags=["Usuários"])
