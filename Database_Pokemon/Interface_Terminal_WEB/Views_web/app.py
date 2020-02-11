import sys

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Projetos-Testes\Database_Pokemon\Interface_Terminal_WEB')

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True, port=80)
