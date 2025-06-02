from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Medicamento(Base):
    __tablename__ = 'medicamentos'

    medicamento_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    exame_clinico = Column(Integer, ForeignKey('exames_clinicos.exame_id'), nullable=False)
    exame_imagem = Column(Integer, ForeignKey('exames_imagem.exame_id'), nullable=False)
    descricao = Column(String(100))

