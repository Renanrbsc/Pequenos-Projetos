from flask import Flask, render_template, request, redirect
import sys

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')
sys.path.append(r'C:\Users\900159\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')

from Controller_Terminal.pokemon_controller import PokemonController
from Controller_Terminal.administrator_controller import AdministratorController

app = Flask(__name__)
login = []

@app.route('/')
def index():
    return render_template('menu_escolha.html', login = None)



@app.route('/login')
def login_admin():
    return render_template('login.html')


@app.route('/menuadmin')
def menu_admin():
    if login:
        return render_template('menu_admin.html')
    else:
        Admin_controller = AdministratorController()
        admin_all = Admin_controller.get_all()
        username = request.args['username']
        passwd = request.args['password']

        for admin in admin_all:
            if str(username).lower() == str(admin.username).lower() \
                    or str(username).lower() == str(admin.email).lower():
                if passwd == str(admin.password).lower():
                    login.append(username)
                    login.append(passwd)
                    return render_template('menu_admin.html')
        return redirect('/login')


@app.route('/menuadminpokemon')
def menu_admin_pokemon():
    if not login:
        return redirect('/login')
    poke = PokemonController()
    lista_dados = poke.get_all()
    lista = []
    for dados in lista_dados:
        lista.append(dados.list())

    return render_template('menu_admin_pokemon.html', lista = lista)

@app.route('/menupokemon')
def listar_todos_pokemon():
    poke = PokemonController()
    lista = poke.get_all()
    lista_nome = []
    for i in lista:
        lista_nome.append(i.nome)

    return render_template('Listar_todos_pokemons.html', lista=lista_nome)


app.run(debug=True, port=80)
