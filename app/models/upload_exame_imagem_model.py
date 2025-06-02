from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class UploadExameImagem(Base):
    __tablename__ = 'uploads_exame_imagem'

    upload_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(45), nullable=False)
    upload = Column(String(45), nullable=False)
    exame_imagem = Column(Integer, ForeignKey('exames_imagem.exame_id'), nullable=False)
