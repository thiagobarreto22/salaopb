from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import genereate_password_hash, check_password_hash

engine = create_engine("sqlite:///server.db")
connection = engine.connect()


session = Session()

Base = declarative_base(engine)


class CriaBanco():
    connection.execute("""CREATE TABLE IF NOT EXISTS USUARIOS (
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255),
                            RUA VARCHAR(255),
                            NUMERO VARCHAR(255),
                            BAIRRO VARCHAR(255),
                            CIDADE VARCHAR(255),
                            ESTADO VARCHAR(255),
                            FONE VARCHAR(255),
                            CPF VARCHAR(255),
                            EMAIL VARCHAR(255),
                            SENHA VARCHAR(255))
                        """)


class Usuarios(Base):
    __tablename__ = 'USUARIOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    fone = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)

    def __init__(
        self,
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
                ):
        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.fone = fone
        self.cpf = cpf
        self.email = email
        self.senha = genereate_password_hash(senha)

    def inserir(
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
                        ):
        usuario = Usuarios(
                    nome,
                    rua,
                    numero,
                    bairro,
                    cidade,
                    estado,
                    fone,
                    cpf,
                    email,
                    senha)
        session.add(usuario)
        session.commit()

    def consulta_usuario(id):
        Consultausuario = session.query(Usuarios).get(id)
        return Consultausuario

    def consulta_email(email):
        retorno = session.query(Usuarios).filter(Usuarios.email == email)
        print(retorno.id)
        return retorno

    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)
