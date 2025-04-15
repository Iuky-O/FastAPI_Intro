from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from app.schemas.testes_schema import Message
from app.controllers.testes_controller import read_html, read_model, read_root

router = APIRouter()

@router.get('/', status_code=HTTPStatus.OK)
def ler_raiz():
    return read_root()

@router.get('/teste_model', status_code=HTTPStatus.OK, response_model=Message)
def ler_com_modelo():
    return read_model()

@router.get('/teste_html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def ler_com_html():
    return read_html()