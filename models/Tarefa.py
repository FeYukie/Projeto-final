tarefas=[] #lista de tarefas

def addTarefa(descricao): #função para adicionar tarefa
    id=len(tarefas)+1 #aumenta a lista
    nova_tarefa=Tarefa(id,descricao) #cria uma nova tarefa
    tarefas.append(nova_tarefa) #adiciona a tarefa na lista
"""Tabelas:
Usuários: Nome, e-mail, senha, tipo de usuário (funcionario ou admin).
Tarefas: Nome da tarefa, descrição, data de vencimento, status (pendente, em andamento, concluído).
Categorias de Tarefa: Classificação das tarefas (pessoal, trabalho, estudo, etc.)//
Disciplinas: Nome da disciplina, professor responsável.
Histórico de Tarefas: Registra as alterações nas tarefas (quem alterou, data da alteração)."""
from database import db

class Tarefa(db.Model):
    __tablename__='livros'
    id=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.Text,nullable=False)
    descricao=db.Column(db.Text,nullable=False)
    data_entrega=db.Column(db.Date, nullable=False)
    completo=db.Column(db.String(20), nullable=False)
    autor_cod=db.Column(db.Integer, db.ForeignKey('autores.cod'),nullable=False)
    cat_id=db.Column(db.Integer, db.ForeignKey('categorias.id'),nullable=False)
    #relacionamento com Autor
    autor=db.relationship('Autor', back_populates='livro')
    #relacionamento com Categoria
    categoria=db.relationship('Categoria', back_populates='livro')

    def __init__(self, id, titulo,descricao,data_entrega,completo=False):
        self.id=id
        self.titulo=titulo
        self.descricao=descricao
        self.data_entrega=data_entrega
        self.status=completo #tarefa concluida


