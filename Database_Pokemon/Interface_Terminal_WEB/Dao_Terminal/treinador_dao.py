from Dao_Terminal.base_dao import BaseDao
from Model_Terminal.treinador_model import TreinadorModel


class TreinadorDao(BaseDao):

    def get_all(self):
        return super().get(TreinadorModel)

    def get_by_id(self, id):
        return super().get(TreinadorModel,id)

    def insert(self, Treinador: TreinadorModel):
        return super().insert(Treinador)

    def update(self, id, Treinador: TreinadorModel):
        Treinador.id = id
        return super().update(Treinador, id)

    def remove(self, id):
        search = super().get(TreinadorModel, id)
        return super().remove(search, id)

