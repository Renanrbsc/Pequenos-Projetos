from flask import Flask, render_template, request, redirect
import sys

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')
sys.path.append(r'C:\Users\900159\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')

from Controller_Terminal.pokemon_controller import PokemonController
from Controller_Terminal.administrator_controller import AdministratorController

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu_escolha():
    Admin_controller = AdministratorController()

    admin_all = Admin_controller.get_all()
    login = request.args['username']
    psswd = request.args['password']
    for admin in admin_all:
        if str(login).lower() == str(admin.username).lower() \
                or str(login).lower() == str(admin.email).lower():
            if psswd == str(admin.password).lower():
                return render_template('menu_escolha.html')
    return redirect('/')


@app.route('/menupokemon')
def listar_todos_pokemon():
    poke = PokemonController()
    lista = poke.get_all()
    lista_nome = []
    for i in lista:
        lista_nome.append(i.nome)

    return render_template('Listar_todos_pokemons.html', lista=lista_nome)


app.run(debug=True, port=80)
