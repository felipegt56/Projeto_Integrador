from sqlalchemy import select, delete,update
from sqlalchemy.orm import Session, query
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario(nome=usuario.nome,
                                    idade=usuario.idade,
                                    cpf=usuario.cpf,
                                    telefone=usuario.telefone)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listar(self):
        query = select(models.Usuario)
        usuarios = self.session.execute(query).scalars().all()
        return usuarios

    def editar(self, id: int, usuario: schemas.Usuario):
        update_stmt = update(models.Usuario).where(
            models.Usuario.id == id).values(nome=usuario.nome,
                                            idade=usuario.idade,
                                            cpf=usuario.cpf,
                                            telefone=usuario.telefone)
        self.session.execute(update_stmt)
        self.session.commit()
    
    def buscarPorId(self, id: int):
        consulta = select(models.Usuario).where(models.Usuario.id == id)
        usuarios = self.session.execute(consulta).first()
        return usuarios
    
    def remover(self, id: int):
        delete_stmt = delete(models.Usuario).where(
            models.Usuario.id == id
        )

        self.session.execute(delete_stmt)
        self.session.commit()