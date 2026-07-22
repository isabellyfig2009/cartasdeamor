from config import db
from modelos.Carta import Carta

class CartaDAO:
    @staticmethod
    def salvar(carta):
        db.session.add(carta)
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Carta.query.all()

    @staticmethod
    def buscar_por_remetente(remetente):
        return Carta.query.filter_by(remetente=remetente).first()

    @staticmethod
    def deletar_carta(obj_carta):
        db.session.delete(obj_carta)
        db.session.commit()