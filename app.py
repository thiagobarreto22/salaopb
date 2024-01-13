
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_login import LoginManager
from werkzeug.security import check_password_hash, generate_password_hash
from model import db, Usuarios, Agendamento
from flask_login import current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'teste'
# db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager(app)

# teste de alt


@app.before_first_request
def create_db():
    db.create_all()


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
        session["usuario"] = usuario.id
        print(usuario)
        if usuario.email == 'admin@admin':
            print(novos_usuarios)
            return redirect(
                'dashboard_gerencial'
                )
        if usuario and check_password_hash(usuario.senha, senha):
            return redirect(url_for('dashboard', usuario_id=usuario.id))
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
    agendamentos = Agendamento.query.filter_by().count()
    novos_usuarios = Usuarios.query.filter_by().count()
    print(agendamentos)
    return render_template('dashboard_gerencial.html',
                           novos_usuarios=novos_usuarios,
                           agendamentos=agendamentos)


@app.route('/dashboard/', methods=["GET", "POST"])
def dashboard():
    if 'usuario' in session:
        usuario = session['usuario']
        print(usuario)
        agendamentos = Agendamento.query.filter_by(id_usuario=usuario).count()
        return render_template('dashboard.html', agendamentos=agendamentos)
    # else:
    #     print('não passou')
    #     return render_template('index.html')


@app.route('/calendar', methods=["GET", "POST"])
def calendar():
    if 'usuario' in session:
        usuario = Usuarios.query.filter_by(id=session['usuario']).first()
        if usuario.email == 'admin@admin':
            return render_template('calendar_gerencial.html')
        else:
            return render_template('calendar.html')


@app.route('/criar_agendamento', methods=["GET", "POST"])
def criar_agendamento():
    if request.method == 'GET':
        return render_template('agendamentos.html')
    else:
        (
            nome,
            email,
            sobrenome,
            telefone,
            dt_agendamento,
            hr_agendamento,
            cabeleleiro,
        ) = (
            request.form.get('nome'),
            request.form.get('email'),
            request.form.get('sobrenome'),
            request.form.get('telefone'),
            request.form.get('dt_agendamento'),
            request.form.get('hr_agendamento'),
            request.form.get('cabeleleiro')
            )
        agendamento = Agendamento()
        usuario = Usuarios.query.filter_by(email=email).first()
        agendamento.id_usuario = usuario.id
        agendamento.nome = f'{nome} {sobrenome}'
        agendamento.email = email
        agendamento.sobrenome = sobrenome
        agendamento.fone = telefone
        agendamento.data_agendamento = dt_agendamento
        agendamento.horario_agendamento = hr_agendamento
        agendamento.cabeleleiro = cabeleleiro
        agendamento.data_registro = datetime.now()
        agendamento.save()
        agendamentos = Agendamento.query.filter_by(email=email).count()
        print(agendamentos)
        return render_template('dashboard.html', agendamentos=agendamentos)


@app.route('/lista_usuarios', methods=["GET", "POST"])
def usuarios():
    usuarios = Usuarios.query.filter_by().all()
    return render_template('usuarios.html', usuarios=usuarios)


@app.route('/lista_agendamentos', methods=["GET", "POST"])
def lista_agendamentos():
    if 'usuario' in session:
        usuario = session['usuario']
        lista_agendamentos = Agendamento.query.filter_by(id_usuario=usuario).all()
        return render_template('lista_agendamentos.html', lista_agendamentos=lista_agendamentos)


@app.route('/lista_agendamentos_gerencial', methods=["GET", "POST"])
def lista_agendamentos_gerencial():
    lista_agendamentos = Agendamento.query.filter_by().all()
    return render_template('lista_agendamentos.html', lista_agendamentos=lista_agendamentos)


def init_app(app):
    login_manager.init_app(app)


if __name__ == "main":
    app.run(debug=True)
