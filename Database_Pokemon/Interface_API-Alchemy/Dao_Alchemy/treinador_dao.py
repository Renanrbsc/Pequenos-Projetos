from Dao_Alchemy.base_dao import BaseDao
from Model_Alchemy.treinador_model import TreinadorModel


class TreinadorDao(BaseDao):

    def get_all(self):
        trainer_all = super().get(TreinadorModel)
        list_trainer = []
        for trainer in trainer_all:
            list_trainer.append(self.dict(trainer))
        return list_trainer

    def get_by_id(self, id):
        return self.dict(super().get(TreinadorModel, id))

    def insert(self, Treinador: TreinadorModel):
        return super().insert(Treinador)

    def update(self, Treinador: TreinadorModel):
        id = Treinador.id
        return super().update(Treinador, id)

    def remove(self, id):
        return super().remove(TreinadorModel, id)

    def dict(self, Treinador):
        trainer = {"id": Treinador.id, "nome": Treinador.nome,
                   "sobrenome": Treinador.sobrenome,
                   "idade": Treinador.idade,
                   "cidade": Treinador.cidade,
                   "Treinador_id": Treinador.pokemon_id
                   }
        return trainer
