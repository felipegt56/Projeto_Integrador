from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schema.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_usuario \
    import RepositorioUsuario

#criar_bd()

router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_cadastrado = RepositorioUsuario(session).criar(usuario)
    return usuario_cadastrado


@router.get('/usuarios', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

@router.put('/usuarios/{id}', response_model=Usuario)
def atualizar_usuario(id: int, usuario: Usuario, session: Session = Depends(get_db)):
    RepositorioUsuario(session).editar(id, usuario)
    usuario.id = id
    return usuario

@router.delete('/usuarios/{id}')
def remover_usuario(id: int, session: Session = Depends(get_db)):
    RepositorioUsuario(session).remover(id)
    return {"msg": "Usuário removido com sucesso"}