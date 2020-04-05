from flask import request

from Interface_API_Alchemy.Controller_Alchemy.base_controller import BaseController
from Interface_API_Alchemy.Dao_Alchemy.pokemon_dao import PokemonDao
from Interface_API_Alchemy.Model_Alchemy.pokemon_model import PokemonModel


class PokemonController(BaseController):

    def __init__(self):
        super().__init__(PokemonDao())

    def post(self):
        return super().post(self.carrega_parametros(id))

    def put(self, id):
        return super().put(self.carrega_parametros(id))

    def carrega_parametros(self, id):
        model = PokemonModel()
        if id:
            model.id = id
        model.nome = request.json['nome']
        model.tipo = request.json['tipo']
        model.altura = float(request.json['altura'])
        model.peso = float(request.json['peso'])
        model.categoria = request.json['categoria']
        model.habilidade = request.json['habilidade']
        model.habilidade2 = request.json['habilidade2']
        model.fraqueza = request.json['fraqueza']
        model.fraqueza2 = request.json['fraqueza2']
        model.descricao = request.json['descricao']
        return model