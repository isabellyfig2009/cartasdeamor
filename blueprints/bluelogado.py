from flask import Blueprint, render_template
from dao.carta_dao import CartaDAO # Importação corrigida para o DAO

bplogado = Blueprint('logado', __name__, url_prefix='/logado')

@bplogado.route('/logado/<nome_usuario>', methods=['GET'])
def logado(nome_usuario):
    todas_cartas = CartaDAO.listar_todos()

    recebidas = []
    enviadas = []

    for carta in todas_cartas:
        if carta.destinatario == nome_usuario:
            recebidas.append(carta)
        if carta.remetente == nome_usuario:
            enviadas.append(carta)

    return render_template('logado.html', usuario=nome_usuario, recebidas=recebidas, enviadas=enviadas)