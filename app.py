
from flask import Flask, render_template, redirect, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from model import Usuarios

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


class Login:
    id = ...
    user = ...
    password = ...

    def get_id(self, id):
        return id


@login_manager.user_loader
def userLoader(id):
    ...


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login-v2.html')


@app.route('/logout', methods=["GET", "POST"])


@app.route('/cadastrar')
def cadastrar():
    return render_template('register.html')


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

        Usuarios.inserir(
                nome,
                rua,
                numero,
                bairro,
                cidade,
                estado,
                fone,
                cpf,
                email,
                senha
                )
    return redirect('/dashboard')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')


@app.route('/calendar', methods=["GET", "POST"])
def calendar():
    return render_template('calendar.html')


def init_app(app):
    login_manager.init_app(app)


app.run(debug=True)
