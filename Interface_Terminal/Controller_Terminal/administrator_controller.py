from Interface_Terminal.Dao_Terminal.administrator_dao import AdministratorDao
from Interface_Terminal.Controller_Terminal.base_controller import BaseController


class AdministratorController(BaseController):
    def __init__(self):
        super().__init__(AdministratorDao())

    def get_all(self):
        return super().get()

    def get_by_id(self, id):
        return super().get(id)

    def post(self, Administrator):
        return super().post(Administrator)

    def put(self, id, Administrator):
        return super().put(id, Administrator)

    def delete(self, id):
        return super().delete(id)
