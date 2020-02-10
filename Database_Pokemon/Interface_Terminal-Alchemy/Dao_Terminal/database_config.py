import MySQLdb


class DatabaseConfig:
    def __init__(self, table):
        host = '127.0.0.1'
        database = 'Pokedex'
        user = 'root'
        self.table = table
        self.connection = MySQLdb.connect(host=host, database=database, user=user)
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table}")
        data_all = self.cursor.fetchall()
        return data_all

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE ID = {id}")
        data = self.cursor.fetchone()
        return data

    def insert(self, command_sql):
        self.cursor.execute(command_sql)
        self.connection.commit()
        id = self.cursor.lastrowid
        return id

    def update(self, command_sql):
        self.cursor.execute(command_sql)
        self.connection.commit()

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM {self.table} WHERE ID = {id}")
        self.connection.commit()
        return f'Removido o id: {id} da tabela {self.table}.'
