from Interface_Terminal.Dao_Terminal.base_dao import BaseDao
from Interface_Terminal.Model_Terminal.pokemon_model import PokemonModel


class PokemonDao(BaseDao):

    def get_all(self):
        return super().get(PokemonModel)

    def get_by_id(self, id):
        return super().get(PokemonModel,id)

    def get_image(self):
        return super().get_image(PokemonModel)

    def insert(self, Pokemon: PokemonModel):
        return super().insert(Pokemon)

    def update(self, id, Pokemon: PokemonModel):
        Pokemon.id = id
        return super().update(Pokemon, id)

    def remove(self, id):
        search = super().get(PokemonModel, id)
        return super().remove(search, id)
