from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schema.schemas import Empresa
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_empresa \
    import RepositorioEmpresa

#criar_bd()

router = APIRouter()

@router.post('/empresas', status_code=status.HTTP_201_CREATED, response_model=Empresa)
def cadastro(empresa: Empresa, session: Session = Depends(get_db)):
    cadastrada_feito = RepositorioEmpresa(session).cadastrar(empresa)
    return cadastrada_feito

@router.get('/empresas', response_model=List[Empresa])
def listar_empresas(session: Session = Depends(get_db)):
    mostra = RepositorioEmpresa(session).listar()
    return mostra

@router.put('/empresas/{id}', response_model=Empresa)
def atualizar_empresa(id: int, empresa: Empresa, session: Session = Depends(get_db)):
    RepositorioEmpresa(session).editar(id, empresa)
    empresa.id = id
    return empresa

@router.delete('/empresas/{id}')
def remover_empresa(id: int, session: Session = Depends(get_db)):
    RepositorioEmpresa(session).remover(id)
    return {"msg": "Empresa removida com sucesso"}