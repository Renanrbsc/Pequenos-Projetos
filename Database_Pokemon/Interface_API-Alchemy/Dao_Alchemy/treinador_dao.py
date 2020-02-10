import MySQLdb

from Model_Alchemy.treinador_model import TreinadorModel
from Dao_Alchemy.base_dao import BaseDao


class TreinadorDao(BaseDao):

    def get_all(self):
        return super().get(TreinadorModel)

    def get_by_id(self, id):
        return super().get(TreinadorModel, id)

    def insert(self, Treinador: TreinadorModel):
        return super().insert(Treinador)

    def update(self, Treinador: TreinadorModel):
        id = Treinador.id
        return super().update(Treinador, id)

    def remove(self, id):
        return super().remove(TreinadorModel, id)
