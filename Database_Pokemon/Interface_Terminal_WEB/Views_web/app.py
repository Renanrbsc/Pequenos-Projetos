from flask import Flask, render_template
import sys

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')
sys.path.append(r'C:\Users\900159\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')

from Controller_Terminal.pokemon_controller import PokemonController

app = Flask(__name__)


@app.route('/')
def index():
    poke = PokemonController()
    lista = poke.get_all()
    lista_nome = []
    for i in lista:
        lista_nome.append(i.nome)

    return render_template('index.html', lista = lista_nome)


app.run(debug=True, port=80)