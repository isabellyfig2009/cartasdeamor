from flask import Blueprint, render_template, request, redirect, url_for
from dao.usuario_dao import UsuarioDAO
from config import db
from dao.carta_dao import CartaDAO


admin = Blueprint('admin', __name__, url_prefix='/admin')

LOGIN_ADMIN = 'admin'
SENHA_ADMIN = '123'

@admin.route('/painel')
def painel_admin():
    usuarios = UsuarioDAO.listar_todos()
    return render_template('adm.html', lista_usuarios=usuarios)


@admin.route('/login')
def abrirloginadmin():
    return render_template('loginadmin.html')

@admin.route('/fazerlogin', methods=['POST'])
def fazerloginadmin():
    login = request.form.get('loginadmin')
    senha = request.form.get('senhaadmin')

    if login == "admim" and senha == "admim":
        return render_template('adm.html')

    texto = 'Login de administrador incorreto'
    return render_template('loginadmin.html', msg=texto)


@admin.route('/listar')
def listar():
    todos_usuarios = UsuarioDAO.listar_todos()
    return render_template('usuariosadmim.html', lista_usuarios=todos_usuarios)


@admin.route('/deletar_usuario/<int:id_usuario>', methods=['POST'])
def deletar_usuario(id_usuario):
    usuario = UsuarioDAO.buscar_por_login(request.form.get('login_usuario'))

    from modelos.usuarios import Usuario
    user_to_delete = Usuario.query.get(id_usuario)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()

    return redirect(url_for('admin.listar'))

@admin.route('/usuarios')
def ver_usuarios_texto():
    return "Lista de usuários"


@admin.route('/cartas')
def ver_cartas_texto():
    todas_cartas = CartaDAO.listar_todos()

    return render_template('cartas.html', cartas=todas_cartas)