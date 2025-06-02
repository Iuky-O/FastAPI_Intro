from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class AnaliseExameImagem(Base):
    __tablename__ = 'analises_exame_cimagem'

    analise_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(40), nullable=False)
    data_analise = Column(String(20), nullable=False)

    predicao = Column(Integer, ForeignKey('predicoes_risco_exame_imagem.predicao_id'), nullable=False)