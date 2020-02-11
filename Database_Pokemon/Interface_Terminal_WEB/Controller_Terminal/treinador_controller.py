from flask import request

from Dao_Terminal.treinador_dao import TreinadorDao
from Model_Terminal.treinador_model import TreinadorModel
from Controller_Terminal.base_controller import BaseController


class TreinadorController(BaseController):
    def __init__(self):
        super().__init__(TreinadorDao())

    def get_all(self):
        return super().get()

    def get_by_id(self, id):
        return super().get(id)

    def post(self, Treinador):
        return super().post(Treinador)

    def put(self, id, Treinador):
        return super().put(id, Treinador)

    def delete(self, id):
        return super().delete(id)
