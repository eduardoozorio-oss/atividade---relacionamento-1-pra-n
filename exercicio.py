from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Motorista(Base):
    __tablename__ = "motorista"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)