from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

class HabitosVida(Base):
    __tablename__ = 'habitos_vida'

    habitos_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero_parceiros = Column(Integer, nullable=True)
    primeira_relacao = Column(Integer, nullable=True)
    numero_gravidez = Column(Integer, nullable=True)

    fuma = Column(Boolean, nullable=True)
    fuma_anos = Column(Integer, nullable=True)

    contraceptivo_hormonal = Column(Boolean, nullable=True)
    contraceptivo_hormonal_anos = Column(Integer, nullable=True)

    diu = Column(Boolean, nullable=True)
    diu_anos = Column(Integer, nullable=True)

    prontuario = Column(Integer, ForeignKey('prontuarios.prontuario_id'), nullable=False)

