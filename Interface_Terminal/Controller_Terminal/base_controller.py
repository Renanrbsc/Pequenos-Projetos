class BaseController:

    def __init__(self, Model):
        self.dao = Model

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def get_image(self):
        return self.dao.get_image()

    def post(self, Model):
        return self.dao.insert(Model)

    def put(self, id, Model):
        return self.dao.update(id, Model)

    def delete(self, id):
        return self.dao.remove(id)

