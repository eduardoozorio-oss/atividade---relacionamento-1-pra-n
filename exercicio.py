from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# -------------------- MOTORISTA --------------------
class Motorista(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    viagens = relationship("Viagens", back_populates="motorista")

    def __repr__(self):
        return f"- Motorista: id={self.id} - nome={self.nome}"


# -------------------- VIAGENS --------------------
class Viagens(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    motorista_id = Column(Integer, ForeignKey("motoristas.id"))

    motorista = relationship("Motorista", back_populates="viagens")

    def __repr__(self):
        return f"- Viagem: id={self.id} - nome={self.nome}"


# -------------------- BANCO --------------------
engine = create_engine("sqlite:///sistema_motorista.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# -------------------- FUNÇÕES --------------------
def cadastrar_motorista():
    with Session() as session:
        try:
            nome = input("Digite o nome do motorista: ").capitalize()

            motorista = Motorista(nome=nome)
            session.add(motorista)
            session.commit()

            print("Motorista cadastrado com sucesso!")

        except Exception as erro:
            session.rollback()
            print(f"Erro: {erro}")


def listar_motoristas():
    with Session() as session:
        motoristas = session.query(Motorista).all()
        for m in motoristas:
            print(m)


