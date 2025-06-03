from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Medicamento(Base):
    __tablename__ = 'medicamentos'

    medicamento_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descricao = Column(String(100))
    
    exame_clinico_id = Column(Integer, ForeignKey('exames_clinicos.exame_id'), nullable=False)
    exame_imagem_id = Column(Integer, ForeignKey('exames_imagem.exame_id'), nullable=False)
    
    #RELACIONAMENTO
    exame_clinico = relationship("ExamesClinicos", back_populates="medicamento")
    exame_imagem = relationship("ExameImagem", back_populates="medicamento")

