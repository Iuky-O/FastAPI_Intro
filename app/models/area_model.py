from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Area(Base):
    __tablename__ = "areas"

    id_area = Column(Integer, primary_key=True, index=True)
    nome = Column(String(45), nullable=False)
    status = Column(String(45), nullable=False)
    especialidade = Column(String(45), nullable=False)