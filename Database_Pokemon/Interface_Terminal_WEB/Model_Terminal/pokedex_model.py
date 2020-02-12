import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from Model_Terminal.treinador_model import TreinadorModel
from Model_Terminal.pokemon_model import PokemonModel

BaseAlchemy = declarative_base()


class PokedexModel(BaseAlchemy):
    __tablename__ = "POKEDEX"

    registro = db.Column(db.Integer, primary_key=True)
    versao = db.Column(db.String(length=100))
    cor = db.Column(db.String(length=100))
    treinador_id = db.Column(db.Integer, db.ForeignKey("TREINADOR.id"))
    pokemon_id = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
    pokemon_id2 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))

    def __init__(self,registro=None):
        self.registro = registro
        self.versao = input("Digite a verao da pokedex: ")
        self.cor = input("Digite a cor da pokedex: ")
        self.treinador_id = input("Digite a ID do treinador: ")
        self.pokemon_id = input("Digite a ID do pokemon: ")
        self.pokemon_id2 = input("Digite a ID do pokemon: ")

    def __str__(self):
        return f"""Registro: {self.registro}
Versao: {self.versao}
Cor: {self.cor}
Treinador ID: {self.treinador_id}
Pokemon1 ID: {self.pokemon_id}
Pokemon2 ID: {self.pokemon_id2}\n
"""
