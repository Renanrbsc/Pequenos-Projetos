class Carro:
	def __init__(self, placa, ano, cor, quilometragem, modelo, marca, registro=None):
		self.registro = registro
		self.placa = placa
		self.ano = ano
		self.cor = cor
		self.quilometragem = quilometragem
		self.modelo = modelo
		self.marca = marca