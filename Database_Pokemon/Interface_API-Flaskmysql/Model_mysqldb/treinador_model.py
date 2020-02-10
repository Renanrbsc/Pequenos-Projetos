class TreinadorModel:
    def __init__(self, nome, sobrenome, idade, cidade, id_pokemon=None, id=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.id_pokemon = id_pokemon
