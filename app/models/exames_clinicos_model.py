from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

class ExamesClinicos(Base):
    __tablename__ = 'exames_clinicos'

    exame_id = Column(Integer, primary_key=True, autoincrement=True)
    
    ist = Column(Boolean, nullable=True)
    ist_numero = Column(Integer, nullable=True)
    ist_hiv = Column(Boolean, nullable=True)
    ist_diagnosticadas_num = Column(Integer, nullable=True)

    diagnostico_cancer = Column(Boolean, nullable=True)
    diagnostico_cin = Column(Boolean, nullable=True)
    diagnostico_hpv = Column(Boolean, nullable=True)
    diagnostico = Column(Boolean, nullable=True)

    hinselmann = Column(Boolean, nullable=True)
    schiller = Column(Boolean, nullable=True)
    citologia = Column(Boolean, nullable=True)
    biopsia = Column(Boolean, nullable=True)

    medicamento = relationship("Medicamento", back_populates="exame_clinico")

