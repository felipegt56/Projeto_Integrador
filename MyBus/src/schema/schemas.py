from pydantic import BaseModel
from typing import Optional, List

class PassagemSimples(BaseModel):
    id: Optional[int] = None
    embarque: str
    desembarque: str

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    cpf: str

    class Config:
        orm_mode = True

class Passagem(BaseModel):
    id: Optional[int] = None
    embarque: str
    desembarque: str
    dia_mes: str
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]
    
    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    cpf: str
    telefone: str
    passagens: List[PassagemSimples] = []

    class Config:
        orm_mode = True

class Empresa(BaseModel):
    id: Optional[int] = None
    nome: str
    de: str
    para: str
    valor: float

    class Config:
        orm_mode = True