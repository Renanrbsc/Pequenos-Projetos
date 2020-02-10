import sys
from flask import Flask
from flask_restful import Api

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_API-Flaskmysql')

from Controller_mysqldb.treinador_controller import TreinadorController
from Controller_mysqldb.pokemon_controller import PokemonController


app = Flask(__name__)
api = Api(app)

api.add_resource(TreinadorController, '/api/treinador', endpoint='treinadores')
api.add_resource(TreinadorController, '/api/treinador/<int:id>', endpoint='treinador')

api.add_resource(PokemonController, '/api/pokemon', endpoint='pokemons')
api.add_resource(PokemonController, '/api/pokemon/<int:id>', endpoint='pokemon')


app.run(debug=True)
