from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship

class DoencaProntuario(Base):
    __tablename__ = "doenca_prontuario"

    doenca_prontuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doenca_id = Column(Integer, ForeignKey('doencas.doenca_id'), nullable=False)
    prontuario_id = Column(Integer, ForeignKey('prontuarios.prontuario_id'), nullable=False)

    # RELACIONAMENTOS
    doenca = relationship("Doencas", back_populates="doenca_prontuarios")
    prontuario = relationship("Prontuario", back_populates="doenca_prontuarios")