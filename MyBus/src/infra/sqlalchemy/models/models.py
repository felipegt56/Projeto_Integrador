from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String)
    telefone = Column(String)

    passagens = relationship('Passagem', back_populates='usuario')

class Passagem(Base):
    __tablename__ = 'passagem'

    id = Column(Integer, primary_key=True, index=True)
    embarque = Column(String)
    desembarque = Column(String)
    dia_mes = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('Usuario', back_populates='passagens')

class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cnpj = Column(String)