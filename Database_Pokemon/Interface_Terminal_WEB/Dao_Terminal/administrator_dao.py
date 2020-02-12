from Dao_Terminal.base_dao import BaseDao
from Model_Terminal.administrator_model import AdministratorModel


class AdministratorDao(BaseDao):

    def get_all(self):
        return super().get(AdministratorModel)

    def get_by_id(self, id):
        return super().get(AdministratorModel,id)

    def insert(self, administrator: AdministratorModel):
        return super().insert(administrator)

    def update(self, id, administrator: AdministratorModel):
        administrator.id = id
        return super().update(administrator, id)

    def remove(self, id):
        search = super().get(AdministratorModel, id)
        return super().remove(search, id)

