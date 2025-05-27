from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Administrador(Base):
    __tablename__ = "admin"

    id_admin = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)