from flask_sqlalchemy import SQLAlchemy 

db=SQLAlchemy()

def inicializa_db(app):
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://estudante1:senha123@localhost:3306/tarefa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        db.create_all()
      