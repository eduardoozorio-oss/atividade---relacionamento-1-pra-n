from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()



inscricao = Table(
    "inscricoes", # nome da tabela
    Base.metadata, #Registro da tabela para ser criado com create_all
    Column("motorista_id", Integer, ForeignKey("motorista.id"), primary_key=True),
    Column("viagens_id", Integer, ForeignKey("viagens.id"), primary_key=True)
)

class Motorista(Base):
    __tablename__ = "motorista"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    viagens = relationship("Viagens", secondary=inscricao, back_populates="estudantes")


    def __repr__(self):
        return f"- Motorista: id= {self.id} - nome: {self.nome}"
    


class Viagens(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    viagens = relationship("Viagens", secondary=inscricao, back_populates="estudantes")


    def __repr__(self):
        return f"- Viagens : id= {self.id} - nome: {self.nome}"
  
engine = create_engine("sqlite:///sistema_motorista.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

