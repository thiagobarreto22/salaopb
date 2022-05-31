from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Usuarios(db.Model):
    __tablename__ = 'USUARIOS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(length=255), nullable=False)
    rua = db.Column(db.String(length=255), nullable=False)
    numero = db.Column(db.String(length=10), nullable=False)
    bairro = db.Column(db.String(length=255), nullable=False)
    cidade = db.Column(db.String(length=255), nullable=False)
    estado = db.Column(db.String(length=255), nullable=False)
    fone = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=255), nullable=False)
    senha = db.Column(db.String(length=200), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def consulta_usuario(id):
    #     return session.query(Usuarios).filter(Usuarios.id == id).first()

# def consulta_email(email):
#     return session.query(Usuarios).filter(Usuarios.email == email).first()

    # def verifica_senha(self, id, senha):
    #     consulta_id = Usuarios.consulta_usuario(id)
    #     if check_password_hash(senha, consulta_id):
    #         return True


class Agendamento(db.Model):
    __tablename__ = 'AGENDAMENTO'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('USUARIOS.id'))
    nome = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=255), nullable=False)
    fone = db.Column(db.String(length=50), nullable=False)
    data_agendamento = db.Column(db.String(length=10), nullable=False)
    horario_agendamento = db.Column(db.String, nullable=False)
    cabeleleiro = db.Column(db.String, nullable=False)
    data_registro = db.Column(db.DateTime, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
