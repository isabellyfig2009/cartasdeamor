from flask import *
from config import db
from blueprints.blueadmin import admin
from blueprints.bluelogado import bplogado
from blueprints.blueusuario import usuario_bp

app = Flask(__name__)
app.secret_key = 'KJ#H4k3jh412dasd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(admin)
app.register_blueprint(usuario_bp)
app.register_blueprint(bplogado)


@app.route('/')
def inicial():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def logar():
    login = request.form.get('login')
    senha = request.form.get('senha')
    if login == 'rene' and senha == '123':
        session['usuario'] = login
        return render_template('logado.html')
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicial'))

@app.route('/verCartas')
def verminhascartas():
    if 'usuario' in session:
        return render_template('enviadas.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)