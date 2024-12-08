from flask import Flask
from database import db, inicializa_db
from controllers.tarefa_controller import tarefas_controller

app = Flask(__name__) 
app.register_blueprint(tarefas_controller)
inicializa_db(app)

if __name__ == '__main__':
  app.run(debug=True)

