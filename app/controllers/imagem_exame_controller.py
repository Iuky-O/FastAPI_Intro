from sqlalchemy.orm import Session
from app.schemas.exame_imagem_schema import ExameImagemUpdate, ExameImagemBase
from app.models.exame_imagem_model import ExameImagem
from fastapi import HTTPException

def criar_exames_imagem(db: Session, exame_imagem: ExameImagemBase):
    novo_exame_imagem = ExameImagem(**exame_imagem.dict())
    db.add(novo_exame_imagem)
    db.commit()
    db.refresh(novo_exame_imagem)
    return novo_exame_imagem

def listar_exames_imagem(db: Session):
    return db.query(ExameImagem).all()

def listar_exames_imagem_id(db: Session, exame_id: int):
    exame = db.query(ExameImagem).filter(ExameImagem.exame_id == exame_id).first()
    if not exame:
        raise HTTPException(status_code=404, detail="Imagem Exame não encontrado")
    return exame
    
def alterar_exame_imagem(db: Session, exame_id: int, dados: ExameImagemUpdate):
    exame = db.query(ExameImagem).filter(ExameImagem.exame_id == exame_id).first()
    if not exame:
        raise HTTPException(status_code=404, detail="Imagem Exame não encontrado")
    
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(exame, key, value)

    db.commit()
    db.refresh(exame)
    return exame

def apagar_exame_imagem(db: Session, exame_id: int):
    exame = db.query(ExameImagem).filter(ExameImagem.exame_id == exame_id).first()
    if not exame:
        raise HTTPException(status_code=404, detail="Imagem Exame não encontrado")
    
    db.delete(exame)
    db.commit()
