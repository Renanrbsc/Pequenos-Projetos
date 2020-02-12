from Dao_Terminal.base_dao import BaseDao
from Model_Terminal.pokedex_model import PokedexModel


class PokedexDao(BaseDao):

    def get_all(self):
        return super().get(PokedexModel)

    def get_by_id(self, id):
        return super().get(PokedexModel,id)

    def insert(self, Pokedex: PokedexModel):
        return super().insert(Pokedex)

    def update(self, id, Pokedex: PokedexModel):
        Pokedex.id = id
        return super().update(Pokedex, id)

    def remove(self, id):
        search = super().get(PokedexModel, id)
        return super().remove(search, id)

