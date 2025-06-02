from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Historico(Base):
    __tablename__ = 'historicos'

    historico_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    modificacao = Column(String(45), nullable=False)
    data_modificacao = Column(String(20), nullable=False)
    prontuario = Column(Integer, ForeignKey('prontuarios.prontuario_id'), nullable=False)
