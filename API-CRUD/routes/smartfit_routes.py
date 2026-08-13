from flask import Blueprint, request
from controllers.smartfit_controllers import get_smartfit, create_smartfit

jogo_routes = Blueprint('alunos_routes', __name__)

@jogo_routes.route('/Alunos', methods=['GET'])
def smartfits_get():
    return get_smartfit()

@jogo_routes.route('/Alunos/<int:alunos_id>', methods=['PUT'])
def smartfits_get_by_id(smartfit_id):
    return get_smartfit_by_id(smartfit_id)

@jogo_routes.route('/Alunos', methods=['POST'])
def smartfits_post():
    return create_smartfit(request.json)

@jogo_routes.route('/Alunos/<int:aluno_id>', methods=['DELETE'])
def smartfits_post():
    return create_aluno(request.json)