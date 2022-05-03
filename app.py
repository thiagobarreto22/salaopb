
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from model import Inserir

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get('nome')
        rua = request.form.get('rua')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        fone = request.form.get('fone')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        senha = request.form.get('senha')

        Inserir(nome, rua, numero, bairro, cidade, estado, fone, cpf, email, senha)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
