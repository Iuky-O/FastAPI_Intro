from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from http import HTTPStatus
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.controllers.upload_exame_imagem_controller import (
    criar_upload_exame_imagem,
    listar_uploads,
    buscar_upload_por_id,
    atualizar_upload,
    apagar_upload
)
from app.schemas.upload_imagem_exame_schema import UploadExameImagemPublic, UploadExameImagemUpdate, UploadExameImagemCreate
from app.services.upload_service import salvar_arquivo_upload
from app.config import settings
from app.dependencies.auth import get_current_user
from app.schemas.usuario_schema import UserPublic
from app.models.medico_model import Medico

router = APIRouter()

@router.post("/", status_code=HTTPStatus.CREATED, response_model=UploadExameImagemPublic)
async def upload_exame_imagem(
    titulo: str = Form(...),
    exame_imagem_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    usuario: UserPublic = Depends(get_current_user),
):
    medico = db.query(Medico).filter(Medico.usuario_id == usuario.usuario_id).first()
    if not medico:
        raise HTTPException(status_code=403, detail="Erro, você não é um médico autorizado!")

    filename = salvar_arquivo_upload(file, settings.security.UPLOAD_DIR)

    dados_upload = UploadExameImagemCreate(
        titulo=titulo,
        exame_imagem_id=exame_imagem_id,
        upload=filename
    )

    resultado = criar_upload_exame_imagem(db, dados_upload, user_id=usuario.usuario_id)

    return resultado


@router.get("/", response_model=list[UploadExameImagemPublic])
def listar(db: Session = Depends(get_db)):
    return listar_uploads(db)


@router.get("/{upload_id}", response_model=UploadExameImagemPublic)
def buscar_por_id(upload_id: int, db: Session = Depends(get_db)):
    return buscar_upload_por_id(db, upload_id)


@router.put("/{upload_id}", response_model=UploadExameImagemPublic)
def atualizar(
    upload_id: int,
    dados: UploadExameImagemUpdate,
    db: Session = Depends(get_db)
):
    return atualizar_upload(db, upload_id, dados)


@router.delete("/{upload_id}", status_code=HTTPStatus.NO_CONTENT)
def deletar(upload_id: int, db: Session = Depends(get_db)):
    apagar_upload(db, upload_id)
    return None
