from sqlalchemy import select, delete,update
from sqlalchemy.orm import Session, query
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositorioEmpresa():

    def __init__(self, session: Session):
        self.session = session

    def cadastrar(self, empresa: schemas.Empresa):
        empresa_db = models.Empresa(nome=empresa.nome,
                                    de=empresa.de,
                                    para=empresa.para,
                                    valor=empresa.valor
                                    )
        self.session.add(empresa_db)
        self.session.commit()
        self.session.refresh(empresa_db)
        return empresa_db

    def listar(self):
        query = select(models.Empresa)
        empresas = self.session.execute(query).scalars().all()
        return empresas

    def buscarPorId(self, id: int):
        query = select(models.Empresa).where(models.Empresa.id == id)
        empresas = self.session.execute(query).scalars().first()
        return empresas

    def editar(self, id: int, empresa: schemas.Empresa):
        update_stmt = update(models.Empresa).where(
            models.Empresa.id == id).values(
                                            nome=empresa.nome,
                                            de=empresa.de,
                                            para=empresa.para,
                                            valor=empresa.valor
                                            )
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id: int):
        delete_stmt = delete(models.Empresa).where(
            models.Empresa.id == id
        )
        
        self.session.execute(delete_stmt)
        self.session.commit()