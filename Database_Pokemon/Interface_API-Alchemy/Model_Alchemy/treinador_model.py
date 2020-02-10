import sqlalchemy as db
from sqlalchemy.orm import relationships
from sqlalchemy.ext.declarative import declarative_base

from Model_Alchemy.pokemon_model import PokemonModel

BaseAlchemy = declarative_base()


class TreinadorModel(BaseAlchemy):
    __tablename__ = "TREINADOR"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    idade = db.Column(db.Integer)
    cidade = db.Column(db.String(length=100))
    pokemon = relationships(PokemonModel)
    id_pokemon = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))

    """
    FOREIGN KEY (ID_POKEMON) REFERENCES POKEMON (ID)
    """

    def __init__(self, nome, sobrenome, idade, cidade, id_pokemon=None, id=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.id_pokemon = id_pokemon

    def __str__(self):
        return f"""Codigo: {self.id}
Nome: {self.nome}
Sobrenome: {self.sobrenome}
Idade: {int(self.idade)}
Cidade: {self.cidade}
Pokemon Inicial ID: {self.id_pokemon}"""
