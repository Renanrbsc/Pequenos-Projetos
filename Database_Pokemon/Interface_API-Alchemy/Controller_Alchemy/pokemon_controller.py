from flask import request

from Controller_Alchemy.base_controller import BaseController
from Dao_Alchemy.pokemon_dao import PokemonDao
from Model_Alchemy.pokemon_model import PokemonModel


class PokemonController(BaseController):

    def __init__(self):
        super().__init__(PokemonDao())

    def post(self):
        self.carrega_parametros()
        Pokemon = PokemonModel(self.nome, self.tipo, self.altura, self.peso, self.categoria,
                               self.habilidade, self.habilidade2, self.fraqueza, self.fraqueza2, self.descricao)
        return super().post(Pokemon)

    def put(self, id):
        self.carrega_parametros()
        Pokemon = PokemonModel(self.nome, self.tipo, self.altura, self.peso, self.categoria,
                               self.habilidade, self.habilidade2, self.fraqueza, self.fraqueza2, self.descricao,
                               id)
        return super().put(Pokemon)

    def carrega_parametros(self):
        self.nome = request.json['nome']
        self.tipo = request.json['tipo']
        self.altura = float(request.json['altura'])
        self.peso = float(request.json['peso'])
        self.categoria = request.json['categoria']
        self.habilidade = request.json['habilidade']
        self.habilidade2 = request.json['habilidade2']
        self.fraqueza = request.json['fraqueza']
        self.fraqueza2 = request.json['fraqueza2']
        self.descricao = request.json['descricao']
