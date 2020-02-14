import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()


class PokemonModel(BaseAlchemy):
    __tablename__ = "POKEMON"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    tipo = db.Column(db.String(length=50))
    altura = db.Column(db.Float())
    peso = db.Column(db.Float())
    categoria = db.Column(db.String(length=50))
    habilidade = db.Column(db.String(length=10))
    habilidade2 = db.Column(db.String(length=100))
    fraqueza = db.Column(db.String(length=50))
    fraqueza2 = db.Column(db.String(length=50))
    descricao = db.Column(db.String(length=255))


    def __init__(self, id=None):
        self.id = id
        self.nome = input("Digite o nome: ")
        self.tipo = input("Digite o tipo: ")
        self.altura = float(input("Digite a altura: "))
        self.peso = float(input("Digite o peso: "))
        self.categoria = input("Digite a categoria: ")
        self.habilidade = input("Digite a habilidade: ")
        self.habilidade2 = input("Digite a habilidade2: ")
        self.fraqueza = input("Digite a fraqueza: ")
        self.fraqueza2 = input("Digite a fraqueza2: ")
        self.descricao = input("Digite a descricao: ")

    def list(self):
        lista = []
        lista.append(self.id)
        lista.append(self.nome)
        lista.append(self.tipo)
        lista.append(self.altura)
        lista.append(self.peso)
        lista.append(self.categoria)
        lista.append(self.habilidade)
        lista.append(self.habilidade2)
        lista.append(self.fraqueza)
        lista.append(self.fraqueza2)
        lista.append(self.descricao)
        return lista

    def __str__(self):
        descricao = self.descricao.replace('.', '.\n')
        return f"""Codigo: {self.id}
Nome: {self.nome}
tipo: {self.tipo}
Altura: {str(self.altura) + ' m'}
Peso: {str(self.peso) + ' kg'}
Categoria: {self.categoria}
Habilidade: {self.habilidade}
Habilidade2: {self.habilidade}
Fraqueza: {self.fraqueza}
Fraqueza2: {self.fraqueza2}
Descricao: {descricao}\n"""


