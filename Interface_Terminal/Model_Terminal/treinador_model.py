import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


BaseAlchemy = declarative_base()


class TreinadorModel(BaseAlchemy):
    __tablename__ = "TREINADOR"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    idade = db.Column(db.Integer)
    cidade = db.Column(db.String(length=100))

    def __init__(self, id=0):
        self.id = id
        self.nome = input("Digite o nome: ")
        self.sobrenome = input("Digite o sobrenome: ")
        self.idade = input("Digite a idade: ")
        self.cidade = input("Digite a cidade: ")

    def __str__(self):
        return f"""Codigo: {self.id}
Nome: {self.nome}
Sobrenome: {self.sobrenome}
Idade: {int(self.idade)}
Cidade: {self.cidade}\n"""
