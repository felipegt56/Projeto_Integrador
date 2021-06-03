from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session, query
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPassagem():

    def __init__(self, session: Session):
        self.session = session

    def comprar(self, passagem: schemas.Passagem):
        db_passagem = models.Passagem(embarque=passagem.embarque,
                                      desembarque=passagem.desembarque,
                                      dia_mes=passagem.dia_mes,
                                      usuario_id=passagem.usuario_id)
        self.session.add(db_passagem)
        self.session.commit()
        self.session.refresh(db_passagem)
        return db_passagem

    def listar_compradas(self):
        query = select(models.Passagem)
        passagens = self.session.execute(query).scalars().all()
        return passagens
    
    def passagemPorId(self, id: int):
        query = select(models.Passagem).where(models.Passagem.id == id)
        passagens = self.session.execute(query).scalars().first()
        return passagens
    
    def listar_minhas_passagens_por_usuario_id(self, user_id: int):
        localizar_usuario = select(models.Passagem).where(models.Passagem.usuario_id == user_id)
        resultado = self.session.execute(localizar_usuario).scalars().all()
        return resultado

    def remover(self, id: int):
        delete_stmt = delete(models.Passagem).where(
            models.Passagem.id == id
        )

        self.session.execute(delete_stmt)
        self.session.commit()