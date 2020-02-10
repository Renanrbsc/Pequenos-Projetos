from flask import request

from Dao_Alchemy.treinador_dao import TreinadorDao
from Model_Alchemy.treinador_model import TreinadorModel
from Controller_Alchemy.base_controller import BaseController


class TreinadorController(BaseController):
    def __init__(self):
        super().__init__(TreinadorDao())

    def post(self):
        return super().post(self.carrega_parametros())

    def put(self, id):
        return super().put(self.carrega_parametros(id))

    def carrega_parametros(self, id=None):
        model = TreinadorModel()
        if id:
            model.id = id
        model.nome = request.json['nome']
        model.sobrenome = request.json['sobrenome']
        model.idade = int(request.json['idade'])
        model.cidade = request.json['cidade']
        model.id_pokemon = request.json['id_pokemon']
        return model
