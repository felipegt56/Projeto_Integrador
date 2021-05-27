from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
#from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String)
    telefone = Column(String)

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cnpj = Column(String)
    
