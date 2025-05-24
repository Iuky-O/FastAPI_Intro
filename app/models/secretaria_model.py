from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Secretaria(Base):
    __tablename__ = "secretarias"

    id_secretaria = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    rg = Column(String(15), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)