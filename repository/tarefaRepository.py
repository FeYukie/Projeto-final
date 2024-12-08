from dao.tarefaDao import TarefaDao

class TarefaRepository:
    def __init__(self):
        self.tarefaDao = TarefaDao()
        
    def buscarTarefaPorId(self, id):
        return self.tarefaDao.buscarTarefaPorId(id)
    
    def deletarPorTarefaId(self,id):
        return self.tarefaDao.deletarTarefaPorId(id)
    
    def criar_tarefa(self, tarefa_id, titulo, descricao, data_entrega, completo):
        return self.tarefaDao.criar_tarefa(tarefa_id, titulo, descricao, data_entrega, completo)

    def update_tarefa(self, tarefa_id, titulo, descricao, data_entrega, completo):
        return self.tarefaDao.update_tarefa(tarefa_id, titulo, descricao, data_entrega, completo)