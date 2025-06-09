from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Administrador(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)
    usuario = relationship("Usuario", back_populates="admins")