from flask import render_template
from app import app

@app.route("/")
def homePage():
    
    usuario = 'kayque'
    idade = 19
    # criando um dicionário
    dados = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template("index.html", dados = dados)


@app.route("/contatos")
def novaPagina():
    return "Página 2"