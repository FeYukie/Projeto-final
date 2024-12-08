from flask import Flask, Blueprint, jsonify, render_template, request, redirect, url_for #importa as funções do flask
from models.Tarefa import tarefas, addTarefa #importa as funções do models
from database import db
from models.Tarefa import Tarefa
from repository.tarefaRepository import TarefaRepository

tarefas_controller=Blueprint('tarefa', __name__)
tarefaRepository=TarefaRepository()

@tarefas_controller.route('/') #rota
def index():
    return render_template('index.html', tarefas=tarefas) 
  
@tarefas_controller.route('/add', methods=['POST'])
def add_tarefa():
    descricao=request.form['descricao']
    addTarefa(descricao)
    return redirect(url_for('tarefa.index'))
"""
    titulo=request.json.get("titulo")
    data_publicacao=request.json.get("data_publicacao")
    autor=request.json.get("autor")
    categoria=request.json.get("categoria")
    pags=request.json.get("pags")
    nova_tarefa = tarefaRepository.criar_tarefa(titulo, data_publicacao, autor, categoria, pags)
    return jsonify({'ID': nova_tarefa.id, 'título': novo_tarefa.titulo, 'data da publicação': novo_tarefa.data_publicacao, 'autor': novo_tarefa.autor, 'categoria': novo_tarefa.categoria, 'quantidade de páginas': novo_tarefa.pags}), 201
"""
@tarefas_controller.route('/tarefa/<int:tarefa_id>', methods=['PUT'])
def update_tarefa(tarefa_id):
    data = request.get_json()
    titulo = data.get('titulo')#?
    descricao=data.get("descricao")
    data_entrega = data.get('data_entrega')
    completo=data.get("status")
    updated_tarefa = tarefaRepository.update_tarefa(tarefa_id, titulo, descricao, data_entrega, completo)
    if updated_tarefa:
        return jsonify({'ID': updated_tarefa.id, 'título': updated_tarefa.titulo, 'descricao': updated_tarefa.descricao, 'data de entrega': updated_tarefa.data_entrega, 'status': updated_tarefa.completo})
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@tarefas_controller.route("/consultarT", methods=['GET'])
def consultar_tarefas():
    tarefa=TarefaRepository.buscarTarefaPorID()    
    return jsonify(tarefa.toJSON())

@tarefas_controller.route("/consultarT/<int:tarefa_id>", methods=['GET'])
def consultar_tarefa1(tarefa_id):
    tarefas=tarefaRepository.buscarTarefaPorID(tarefa_id)
    tarefasJSON=[]
    for tarefa in tarefas:
        tarefasJSON.append(tarefa.toJSON())
    return jsonify(tarefasJSON)

@tarefas_controller.route("/delT/<int:tarefa_id>", methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    tarefa_deletada = tarefaRepository.deletarTarefaPorID(tarefa_id)
    if tarefa_deletada:
        return jsonify({'message': 'Tarefa deletada!'})
    return jsonify({'error': 'Tarefa não encontrada'}), 404


