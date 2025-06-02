from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Prontuario(Base):
    __tablename__ = 'prontuarios'

    prontuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    consulta = Column(Integer, ForeignKey('consultas.consulta_id'), nullable=False)
    exame_clinico = Column(Integer, ForeignKey('exames_clinicos.exame_id'), nullable=False)
    exame_imagem = Column(Integer, ForeignKey('exames_imagem.exame_id'), nullable=False)
    medicamento = Column(Integer, ForeignKey('medicamentos.medicamento_id'), nullable=False)

