from flask import Blueprint, render_template, request
from database.models.cliente import Clientes

cliente_route = Blueprint('cliente',__name__)

@cliente_route.route('/')
def lista_cliente():
    clientes = Clientes.select()
    return render_template('lista_cliente.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_usuario = Clientes.create(
        nome = data['nome'],
        email = data['email'],)
    return render_template('item_cliente.html', cliente=novo_usuario)    

@cliente_route.route('/new')
def formulario_criar_cliente():
    return render_template('form_c_cliente.html')

@cliente_route.route('/<int:ClienteID>')
def detalhe_cliente(ClienteID):
    cliente = Clientes.get_by_id(ClienteID)
    return render_template('detalhe_cliente.html', cliente=cliente)
 
@cliente_route.route('/<int:ClienteID>/edit')
def formulario_editar_cliente(ClienteID):
    cliente = Clientes.get_by_id(ClienteID)
    return render_template('form_c_cliente.html', cliente=cliente)
          
@cliente_route.route('/<int:ClienteID>/update', methods=['PUT'])
def atualizar_cliente(ClienteID):
    data = request.json
    cliente_editado = Clientes.get_by_id(ClienteID)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente=cliente_editado)
 

@cliente_route.route('/<int:ClienteID>/delete', methods=['DELETE'])
def deletar_cliente(ClienteID):
    cliente = Clientes.get_by_id(ClienteID)
    cliente.delete_instance()