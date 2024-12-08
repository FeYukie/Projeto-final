from models.Tarefa import Tarefa, db

class TarefaDao:
    @staticmethod
    def addTarefa(nome_cat):
        tarefa = Tarefa(nome_cat=nome_cat)
        db.session.add(tarefa)
        db.session.commit()
        return tarefa
    
    @staticmethod
    def editTarefa(id, nome_cat):
        tarefa = Tarefa.buscarTarefaPorId(id)
        if tarefa:
            tarefa.nome_cat = nome_cat
            db.session.commit()
        return tarefa
    
    @staticmethod
    def buscarTarefaPorId(id):
        return Tarefa.query.get(id)
    
    @staticmethod
    def deletarTarefaPorId(id):
        try:
            tarefa=TarefaDao.buscarTarefaPorId(id)
            db.session.delete(id)
            db.session.commit()
            return tarefa.toJSON()
        except Exception as e:
            db.session.rollback()
            return {"erro": "Tarefa não encontrada!"}