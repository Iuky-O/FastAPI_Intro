from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class AnaliseMedicamento(Base):
    __tablename__ = 'analise_medicamentos'

    analise_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(50), nullable=False)
    data_analise = Column(String(20), nullable=False)
    predicao_medicamento = Column(Integer, ForeignKey('predicao_medicamentos.predicao_id'), nullable=False)
