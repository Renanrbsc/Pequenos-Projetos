from Orientacao_Objeto_Python.Exercicio_classes.pessoa import Pessoa, RetornoSalario


class Engenheiro(Pessoa):
    def __init__(self, graduacao, projeto, nome, sobrenome, idade, numero_de_horas_salario,
                 pais, estado, cidade, bairro, rua):

        calcular_salario = RetornoSalario(numero_de_horas_salario, 50)
        super().__init__(nome, sobrenome, idade, calcular_salario.calcular_salario_bruto(),
                         pais, estado, cidade, bairro, rua)

        self.graduacao = graduacao
        self.projeto = projeto

    @property
    def graduacao(self):
        return self._graduacao

    @graduacao.setter
    def graduacao(self, graduacao):
        self._graduacao = graduacao

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, projeto):
        self._projeto = projeto

    def __str__(self):
        return f"----- Engenheiro ----- \n" \
               f"Graduação: {self.graduacao} \n" \
               f"Projeto Atual: {self.projeto} \n" \
               f"{super().__str__()}"
