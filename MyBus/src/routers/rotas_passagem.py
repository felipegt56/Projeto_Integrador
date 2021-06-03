from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schema.schemas import Passagem, PassagemSimples
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_passagem \
    import RepositorioPassagem

#criar_bd()

router = APIRouter()

@router.post('/passagem', status_code=status.HTTP_201_CREATED, response_model=Passagem)
def comprar_passagem(passagem: Passagem, session: Session = Depends(get_db)):
    passagem_comprada = RepositorioPassagem(session).comprar(passagem)
    return passagem_comprada

@router.get('/passagem', response_model=List[PassagemSimples])
def listar(session: Session = Depends(get_db)):
    passagens  = RepositorioPassagem(session).listar_compradas()
    return passagens

@router.get('/passagem/{id}/passagem', response_model=List[Passagem])
def listar_passagem(id: int, session: Session = Depends(get_db)):
    passagens = RepositorioPassagem(session).listar_minhas_passagens_por_usuario_id(id)
    if not  passagens:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário {id} não localizado')
    return passagens

@router.delete('/passagem/{id}')
def excluir_passagem(id: int, session: Session = Depends(get_db)):
    passagem_localizado = RepositorioPassagem(session).passagemPorId(id)
    if not passagem_localizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Passagem com o ID {id} não localizado')
    
    RepositorioPassagem(session).remover(id)
    return {"msg": "Removido com sucesso"}