import sys
from flask import Flask
from flask_restful import Api

from Controller_Alchemy.treinador_controller import TreinadorController
from Controller_Alchemy.pokemon_controller import PokemonController
sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_API-Alchemy')


app = Flask(__name__)
api = Api(app)

api.add_resource(PokemonController, '/api/pokemon', endpoint='pokemons')
api.add_resource(PokemonController, '/api/pokemon/<int:id>', endpoint='pokemon')

api.add_resource(TreinadorController, '/api/treinador', endpoint='treinadores')
api.add_resource(TreinadorController, '/api/treinador/<int:id>', endpoint='treinador')

app.run(debug=True)
