
from flask import Flask, render_template, request
from flask_login import LoginManager, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from model import db, Usuarios

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'teste'
# db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager(app)


@app.before_first_request
def create_db():
    db.create_all()

# class Login:
#     id = ...
#     user = ...
#     password = ...

#     def get_id(self, id):
#         return id


@login_manager.user_loader
def userLoader(id):
    ...


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login-v2.html')
    else:
        email = request.form.get('email')
        senha = request.form.get('senha')
        novos_usuarios = Usuarios.query.filter_by().count()
        usuario = Usuarios.query.filter_by(email=email).first()
        print(usuario)
        if usuario.email == 'admin@admin':
            print(novos_usuarios)
            return render_template('dashboard_gerencial.html', novos_usuarios=novos_usuarios)
        if usuario and check_password_hash(usuario.senha, senha):
            return render_template('dashboard.html')
        else:
            return render_template('login-v2.html')


@app.route('/logout')
# @login_required
def logout():
    # logout_user()
    return render_template('login-v2.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('register.html')


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    (
        nome,
        rua,
        numero,
        bairro,
        cidade,
        estado,
        fone,
        email,
        senha
    ) = (
        request.form.get('nome'),
        request.form.get('rua'),
        request.form.get('numero'),
        request.form.get('bairro'),
        request.form.get('cidade'),
        request.form.get('estado'),
        request.form.get('fone'),
        request.form.get('email'),
        generate_password_hash(request.form.get('senha')),
        )
    usuario = Usuarios()
    usuario.nome = nome
    usuario.rua = rua
    usuario.numero = numero
    usuario.bairro = bairro
    usuario.cidade = cidade
    usuario.estado = estado
    usuario.fone = fone
    usuario.email = email
    usuario.senha = senha
    usuario.save()
    return render_template('login-v2.html')


@app.route('/dashboard_gerencial', methods=["GET", "POST"])
def dashboard_gerencial():
    return render_template('dashboard_gerencial.html')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')
    # else:
    #     print('não passou')
    #     return render_template('index.html')


@app.route('/calendar', methods=["GET", "POST"])
def calendar():
    return render_template('calendar.html')


def init_app(app):
    login_manager.init_app(app)


if __name__ == "main":
    app.run(debug=True)
