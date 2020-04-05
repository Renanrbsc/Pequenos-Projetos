from Interface_API_Alchemy.Dao_Alchemy.base_dao import BaseDao
from Interface_API_Alchemy.Model_Alchemy.pokemon_model import PokemonModel
import json

class PokemonDao(BaseDao):

    def get_all(self):
        pokemon_all = super().get(PokemonModel)
        list_pokemon = []
        for pokemon in pokemon_all:
            list_pokemon.append(pokemon.serialize())
        return list_pokemon

    def get_by_id(self, id):
        pokemon = super().get(PokemonModel, id)
        return pokemon.serialize()

    def insert(self, Pokemon: PokemonModel):
        return super().insert(Pokemon)

    def update(self, Pokemon: PokemonModel):
        id = Pokemon.id
        return super().update(Pokemon, id)

    def remove(self, id):
        return super().remove(PokemonModel, id)

