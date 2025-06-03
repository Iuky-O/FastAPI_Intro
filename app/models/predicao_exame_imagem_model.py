from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class PredicaoExameImagem(Base):
    __tablename__ = 'predicoes_risco_exame_imagem'

    predicao_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    risco = Column(String(10), nullable=False)
    data_analise = Column(String(20), nullable=False)

    analises = relationship("AnaliseExameImagem", back_populates="predicao")
