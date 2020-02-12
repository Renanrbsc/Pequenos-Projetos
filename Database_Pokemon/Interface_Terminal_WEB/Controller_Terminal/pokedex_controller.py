from flask import request

from Dao_Terminal.pokedex_dao import PokedexDao
from Controller_Terminal.base_controller import BaseController


class PokedexController(BaseController):
    def __init__(self):
        super().__init__(PokedexDao())

    def get_all(self):
        return super().get()

    def get_by_id(self, id):
        return super().get(id)

    def post(self, Pokedex):
        return super().post(Pokedex)

    def put(self, id, Pokedex):
        return super().put(id, Pokedex)

    def delete(self, id):
        return super().delete(id)
