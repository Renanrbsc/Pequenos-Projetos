import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:
    def __init__(self):
        # -- formato de string (SGBD+conector://user:passwd@url:port/database)
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/PokedexPokemon")
        criar_sessao = db.orm.sessionmaker()
        criar_sessao.configure(bind=conexao)
        self.sessao = criar_sessao()

    def get(self, Model, id=None)-> list:
        if id:
            return self.sessao.query(Model).filter(Model.id == id).one()
        return self.sessao.query(Model).all()

    def get_image(self, Model):
        return self.sessao.query(Model).filter(Model.nome).all()

    def insert(self, Model)-> str:
        self.sessao.add(Model)
        self.sessao.commit()
        self.sessao.close()
        return 'Adicionado com sucesso!'

    def update(self, new_update, id)-> str:
        self.sessao.merge(new_update)
        self.sessao.commit()
        self.sessao.close()
        return f'Atualizado ID {id} da tabela'

    def remove(self, search, id)-> str:
        self.sessao.delete(search)
        self.sessao.commit()
        self.sessao.close()
        return f'Removido a ID {id} da tabela'
