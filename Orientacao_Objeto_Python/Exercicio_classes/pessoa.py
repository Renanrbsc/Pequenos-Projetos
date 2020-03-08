from Orientacao_Objeto_Python.Exercicio_classes.endereco import Endereco


class RetornoSalario:
    def __init__(self, numero_horas_trabalhadas, salario_por_hora):
        self.numero_horas_trabalhadas = numero_horas_trabalhadas
        self.salario_por_hora = salario_por_hora

    @property
    def numero_horas_trabalhadas(self):
        print(f'Nome: {self._numero_horas_trabalhadas}')
        return self._numero_horas_trabalhadas

    @numero_horas_trabalhadas.setter
    def numero_horas_trabalhadas(self, numero_horas_trabalhadas):
        self._numero_horas_trabalhadas = int(numero_horas_trabalhadas)

    def calcular_salario_bruto(self):
        return self._numero_horas_trabalhadas * self.salario_por_hora


class Pessoa:
    def __init__(self, nome, sobrenome, idade, salario, pais, estado, cidade, bairro, rua):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = salario
        self.endereco = Endereco(pais, estado, cidade, bairro, rua)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        if isinstance(salario, str):
            salario = salario.replace('R$', '')
        self._salario = float(salario)

    def __str__(self):
        return f"----- Dados Pessoais ----- \n" \
               f"Nome: {self.nome} \n" \
               f"Sobrenome: {self.sobrenome} \n" \
               f"Idade: {self.idade} \n" \
               f"Salario: {self.salario} \n" \
               f"----- Endereco ----- \n" \
               f"{self.endereco}"
