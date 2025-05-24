from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Medico(Base):
    __tablename__ = "medicos"

    id_medico = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    rg = Column(String(45), nullable=False)
    especializacao = Column(String(45), nullable=False)
    crm_numero = Column(String(45), nullable=False, unique=True)
    crm_UF = Column(String(45), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    areas_idareas = Column(Integer, ForeignKey("areas.id_area"), nullable=False)
