from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Paciente(Base):
    __tablename__ = "pacientes"

    paciente_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    data_nascimento = Column(String(10), nullable=False)
    rg = Column(String(45), nullable=False)
    cpf = Column(String(45), nullable=False, unique=True)
    data_cadastro = Column(String(45), nullable=False)
    endereco = Column(String(45), nullable=False)
    telefone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    plano_saude = Column(Boolean, nullable=False)

    consultas = relationship("Consulta", back_populates="paciente")
