import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()


class PokedexModel(BaseAlchemy):
    __tablename__ = "POKEDEX"

    registro = db.Column(db.Integer, primary_key=True)
    versao = db.Column(db.String(length=100))
    id_treinador = db.Column(db.Integer, db.ForeignKey("TREINADOR.id"))
    id_pokemon1 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
    id_pokemon2 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
    id_pokemon3 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
    id_pokemon4 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
    id_pokemon5 = db.Column(db.Integer, db.ForeignKey("POKEMON.id"))
