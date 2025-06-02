#Aqui fica o modelo do user (tabela do banco de dados)
from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(45), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    nome = Column(String(45), nullable=False)
    telefone = Column(String(45), nullable=False)