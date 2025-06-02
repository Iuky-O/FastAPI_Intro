from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base

class DoencaProntuario(Base):
    __tablename__ = "doenca_prontuario"

    doenca_prontuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doenca = Column(Integer, ForeignKey('doencas.doenca_id'), nullable=False)
    prontuario = Column(Integer, ForeignKey('prontuarios.prontuario_id'), nullable=False)