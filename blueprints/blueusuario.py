from flask import *
from dao.carta_dao import CartaDAO
from modelos.Carta import Carta
from modelos.usuarios import Usuario
from dao.usuario_dao import UsuarioDAO

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')


@usuario_bp.route('/')
def inicial():
    return render_template('index.html')


@usuario_bp.route('/login', methods=['GET'])
def mostrar_login():
    return render_template('login.html')


@usuario_bp.route('/login', methods=['POST'])
def login():
    nome_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')

    todos_usuarios = UsuarioDAO.listar_todos()
    usuario_encontrado = None

    for u in todos_usuarios:
        if u.login == nome_digitado and u.senha == senha_digitada:
            usuario_encontrado = u
            break

    if usuario_encontrado:
        session['usuario'] = usuario_encontrado.login
        return redirect(f'/usuario/logado/{usuario_encontrado.login}')
    else:
        return redirect('/usuario/login')


@usuario_bp.route('/cadastrar', methods=['POST'])
def fazercadastro():
    nome = request.form.get('nome')
    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    novo_user = Usuario(nome=nome, login=login, senha=senha)
    try:
        UsuarioDAO.salvar(novo_user)
        mensagem = 'Usuário cadastrado com sucesso! Faça login.'
    except Exception as erro:
        print(f"Erro ao cadastrar: {erro}")
        mensagem = 'Erro ao cadastrar. O login informado já existe.'

    return render_template('login.html', mensagem=mensagem)


@usuario_bp.route('/logado')
def pagina_logado():
    if 'usuario' not in session:
        return render_template('login.html', mensagem="Por favor, faça login primeiro.")

    return render_template('logado.html', usuario=session['usuario'])


@usuario_bp.route('/logado/<nome_usuario>', methods=['GET'])
def logado(nome_usuario):
    session['usuario'] = nome_usuario
    todas_cartas = CartaDAO.listar_todos()

    recebidas = []
    enviadas = []

    for carta in todas_cartas:
        if carta.destinatario == nome_usuario:
            recebidas.append(carta)
        if carta.remetente == nome_usuario:
            enviadas.append(carta)

    return render_template('logado.html', usuario=nome_usuario, recebidas=recebidas, enviadas=enviadas)


@usuario_bp.route('/remover/<usuario>', methods=['GET'])
def excluirusuario(usuario):
    obj_user = UsuarioDAO.buscar_por_login(usuario)
    if obj_user:
        UsuarioDAO.remover(obj_user)
    return redirect('/usuario/login')


@usuario_bp.route('/deletar_carta/<deletar_carta>', methods=['GET'])
def deletar_carta(deletar_carta):
    carta_objeto = Carta.query.filter_by(texto=deletar_carta).first()

    if carta_objeto:
        CartaDAO.deletar_carta(carta_objeto)

    usuario_atual = session.get("usuario")
    return redirect(f'/usuario/logado/{usuario_atual}')


@usuario_bp.route('/admin/deletar_carta/<texto_carta>', methods=['GET'])
def admin_deletar_carta(texto_carta):
    carta_objeto = Carta.query.filter_by(texto=texto_carta).first()

    if carta_objeto:
        CartaDAO.deletar_carta(carta_objeto)

    return redirect('/admin/cartas')


@usuario_bp.route('/salvarcarta', methods=['POST'])
def salvar_carta_usuario():
    remetente = request.form.get('usuario')
    destinatario = request.form.get('destinatario')
    texto = request.form.get('texto')
    cor = request.form.get('cor')

    nova_carta = Carta(remetente=remetente, destinatario=destinatario, texto=texto, cor=cor)
    CartaDAO.salvar(nova_carta)

    return redirect(f'/usuario/logado/{remetente}')