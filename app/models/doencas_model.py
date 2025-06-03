from sqlalchemy import Column, Integer, String
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Doencas(Base):
    __tablename__ = "doencas"

    doenca_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    status = Column(String(15), nullable=False)

    doenca_prontuarios = relationship("DoencaProntuario", back_populates="doenca")