from config import db

class Carta(db.Model):
    __tablename__ = 'cartas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    remetente = db.Column(db.String(150), nullable=False)
    destinatario = db.Column(db.String(150), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    cor = db.Column(db.String(50), default='padrao')

    def __init__(self, remetente, destinatario, texto, cor='padrao'):
        self.remetente = remetente
        self.destinatario = destinatario
        self.texto = texto
        self.cor = cor