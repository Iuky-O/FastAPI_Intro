from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class UploadProntuario(Base):
    __tablename__ = 'uploads_prontuario'

    upload_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(45), nullable=False)
    upload = Column(String(45), nullable=False)
    prontuario = Column(Integer, ForeignKey('prontuarios.prontuario_id'), nullable=False)
