from models.smartfit_models import smartfit
from db import db
import json
from flask import make_response, request

def get_smartfit():
    smartfit = smartfit.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de alunos.',
            'dados': [smartfit.json() for smartfit in smartfit]
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def get_smartfit_by_id(smartfit_id):
    smartfits = smartfits.query.get(smartfit_id)

    if smartfits:
        response = make_response(
            json.dumps({
                'mensagem': 'Aluno encontrado.',
                'dados': smartfits.json()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'Aluno não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

def create_smartfit(smartfit_data):
    if not all(key in smartfit_data for key in ['Nome', 'genero', 'Endereço', 'Idade']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos, Nome, gênero, Endereço e idade são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    novo_smartfit = smartfit_data(
        nome=smartfit_data['Nome'],
        genero=smartfit_data['genero'],
        endereco=smartfit_data['endereco'],
        idade=smartfit_data['idade']
    )
    
    db.session.add(novo_smartfit)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Aluno cadastrado com sucesso.',
            'aluno': novo_smartfit.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response