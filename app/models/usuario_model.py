from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(45), unique=True, nullable=False)
    senha = Column(String(80), nullable=False)
    nome = Column(String(45), nullable=False)
    telefone = Column(String(45), nullable=False)

    #Relacionamentos
    medicos = relationship("Medico", back_populates="usuario")
    secretarias = relationship("Secretaria", back_populates="usuario")
    admins = relationship("Administrador", back_populates="usuario")