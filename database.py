from flask_sqlalchemy import SQLAlchemy 

db=SQLAlchemy()

def inicializa_db(app):
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql:///nomedapasta:senha@localhost:3306/nome_do_banco'
    """mysql+pymysql: Usando o driver PyMySQL para se conectar ao MySQL.
    nome da pasta: nome da pasta armazenada para acessar o banco de dados MySQL.
    senha: Sua senha para o banco de dados.
    localhost: O servidor do banco de dados (aqui está localhost, o que significa que o banco de dados está na mesma máquina onde o servidor Flask está rodando).
    3306: O porta padrão do MySQL.
    nome_do_banco: O nome do banco de dados que você criou no MySQL."""
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        db.create_all()
        """tema de Gestão de Tarefas (To-Do List com Níveis de Acesso)
Objetivo: Desenvolver um sistema onde os usuários podem cadastrar tarefas, marcar como concluídas, e visualizá-las em uma lista. Administradores podem gerenciar todos os usuários e tarefas.

Acessos: Funcionarios podem adicionar e marcar como concluidas suas tarefas de estudos, enquanto administradores podem adicionar prazos e materiais complementares.
Sistema de Gestão de Tarefas e Estudos
Objetivo: Criar um sistema onde os estudantes possam funcionarios suas tarefas e compromissos acadêmicos (provas, trabalhos, prazos).

"""