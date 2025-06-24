from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from app.services.upload_service import salvar_arquivo_upload
from app.models.upload_exame_imagem_model import UploadExameImagem
from app.schemas.upload_imagem_exame_schema import UploadExameImagemCreate, UploadExameImagemUpdate
from app.config import settings
import os
from app.models.medico_model import Medico

def criar_upload_exame_imagem(db: Session, dados: UploadExameImagemCreate, user_id: int):
    url_base = settings.security.URL_API
    caminho_completo = f"{url_base}/files/{dados.upload}"

    caminho_arquivo = os.path.join(settings.security.UPLOAD_DIR, dados.upload)
    if not os.path.exists(caminho_arquivo):
        raise HTTPException(status_code=500, detail="Falha ao localizar o arquivo no servidor.")
    
    novo = UploadExameImagem(
        titulo=dados.titulo.strip(),
        exame_imagem_id=dados.exame_imagem_id,
        upload=caminho_completo,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo

def listar_uploads(db: Session):
    return db.query(UploadExameImagem).all()

def buscar_upload_por_id(db: Session, upload_id: int):
    upload = db.query(UploadExameImagem).filter(UploadExameImagem.upload_id == upload_id).first()
    if not upload:
        raise HTTPException(status_code=404, detail="Upload não encontrado")
    return upload

def atualizar_upload(db: Session, upload_id: int, dados: UploadExameImagemUpdate):
    upload = buscar_upload_por_id(db, upload_id)
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(upload, key, value)
    db.commit()
    db.refresh(upload)
    return upload

def apagar_upload(db: Session, upload_id: int):
    upload = buscar_upload_por_id(db, upload_id)
    db.delete(upload)
    db.commit()
