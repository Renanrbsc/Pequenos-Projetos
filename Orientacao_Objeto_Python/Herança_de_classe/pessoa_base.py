class PessoaBase:
    _ano_atual = 2020

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    def nome_completo(self):
        return f'Nome Completo: {self.nome} {self.sobrenome}'

    def ano_de_nascimento(self):
        return f'Ano de nascimento: {self._ano_atual - self.idade}'



