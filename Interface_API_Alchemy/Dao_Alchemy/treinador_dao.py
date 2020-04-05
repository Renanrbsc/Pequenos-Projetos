from Interface_API_Alchemy.Dao_Alchemy.base_dao import BaseDao
from Interface_API_Alchemy.Model_Alchemy.treinador_model import TreinadorModel


class TreinadorDao(BaseDao):

    def get_all(self):
        trainer_all = super().get(TreinadorModel)
        list_trainer = []
        for trainer in trainer_all:
            list_trainer.append(trainer.serialize())
        return list_trainer

    def get_by_id(self, id):
        treinador = super().get(TreinadorModel, id)
        return treinador.serialize()

    def insert(self, Treinador: TreinadorModel):
        return super().insert(Treinador)

    def update(self, Treinador: TreinadorModel):
        id = Treinador.id
        return super().update(Treinador, id)

    def remove(self, id):
        return super().remove(TreinadorModel, id)

