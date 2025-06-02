from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class ExameImagem(Base):
    __tablename__ = 'exames_imagem'

    exame_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(String(45), nullable=False)
    descricao = Column(String(45))
    link_imagem = Column(String(45))


