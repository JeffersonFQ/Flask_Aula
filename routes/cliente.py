from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente',__name__)

@cliente_route.route('/')
def lista_cliente():
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def criar_cliente():
    data = request.json
    novo_usuario = {
        "id" : len(CLIENTES) + 1,
        "nome" : data['nome'],
        "email" : data['email']
    }
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)
    

@cliente_route.route('/new')
def formulario_criar_cliente():
    return render_template('form_c_cliente.html')

@cliente_route.route('/<int:ClienteID>')
def detalhe_cliente(ClienteID):
    return render_template('detalhe_cliente.html')
 
@cliente_route.route('/<int:ClienteID>/edit')
def formulario_editar_cliente(ClienteID):
    return render_template('fomr_e_cliente.html')
          
@cliente_route.route('/<int:ClienteID>/update', methods=['PUT'])
def atualizar_cliente():
    return "Atualizar os dados de um cliente" 

@cliente_route.route('/<int:ClienteID>/delete', methods=['DELETE'])
def deletar_cliente(ClienteID):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != ClienteID ]
    return "Cliente deletado"