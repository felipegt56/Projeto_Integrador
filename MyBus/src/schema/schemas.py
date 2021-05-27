from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    cpf: str
    telefone: str

    class Config:
        orm_mode = True

class Empresa(BaseModel):
    id: Optional[int] = None
    nome: str
    cnpj: str

    class Config:
        orm_mode = True


class nada():
    pass
