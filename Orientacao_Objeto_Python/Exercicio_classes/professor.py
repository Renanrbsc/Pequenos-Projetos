from Orientacao_Objeto_Python.Exercicio_classes.pessoa import Pessoa, RetornoSalario


class Professor(Pessoa):
    def __init__(self, graduacao, periodo, nome, sobrenome, idade, numero_de_horas_salario,
                 pais, estado, cidade, bairro, rua):

        calcular_salario = RetornoSalario(numero_de_horas_salario, 25)
        super().__init__(nome, sobrenome, idade, calcular_salario.calcular_salario_bruto(),
                         pais, estado, cidade, bairro, rua)

        self.graduacao = graduacao
        self.periodo = periodo

    @property
    def graduacao(self):
        return self._graduacao

    @graduacao.setter
    def graduacao(self, graduacao):
        self._graduacao = graduacao

    @property
    def periodo(self):
        return self._periodo

    @periodo.setter
    def periodo(self, periodo):
        self._periodo = periodo

    def __str__(self):
        return f"----- Professor ----- \n" \
               f"Graduação: {self.graduacao} \n" \
               f"Periodo: {self.periodo} \n" \
               f"{super().__str__()}"
