from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class PredicaoMedicamento(Base):
    __tablename__ = 'predicao_medicamentos'

    predicao_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    predicao_medicamento = Column(String(50), nullable=False)
    data_predicao = Column(String(10), nullable=False)
