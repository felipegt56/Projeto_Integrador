from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schema.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_usuario \
    import RepositorioUsuario

#criar_bd()

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_cadastrado = RepositorioUsuario(session).criar(usuario)
    return usuario_cadastrado

@router.get('/usuarios', response_model=List[UsuarioSimples])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

@router.get('/usuario/{id}')
def Buscar_id(id: int, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(session).buscarPorId(id)
    if not usuario_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o ID {id} não localizado')
    return usuario_localizado

@router.put('/usuarios/{id}', response_model=UsuarioSimples)
def atualizar_usuario(id: int, usuario: Usuario, session: Session = Depends(get_db)):
    RepositorioUsuario(session).editar(id, usuario)
    usuario.id = id
    usuario_localizado = RepositorioUsuario(session).buscarPorId(id)
    if not usuario_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o ID {id} não localizado')
    return usuario
    
@router.delete('/usuarios/{id}')
def remover_usuario(id: int, session: Session = Depends(get_db)):
    usuario_localizado = RepositorioUsuario(session).buscarPorId(id)
    if not usuario_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o ID {id} não localizado')
    
    RepositorioUsuario(session).remover(id)
    return {"msg": "Removido com sucesso"}
