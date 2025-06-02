from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Consulta(Base):
    __tablename__ = 'consultas'

    consulta_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data_consulta = Column(String(10), nullable=False)

    medico = Column(Integer, ForeignKey('medicos.medico_id'), nullable=False)
    secretaria = Column(Integer, ForeignKey('secretarias.secretaria_id'), nullable=False)
    paciente = Column(Integer, ForeignKey('pacientes.paciente_id'), nullable=False)
