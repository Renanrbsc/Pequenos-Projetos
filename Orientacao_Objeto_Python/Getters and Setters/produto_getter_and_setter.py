class Produto:
	def __init__(self, nome, novo_valor):
		self.nome = nome
		self.valor = novo_valor

	def desconto(self, percentual):
		self._valor = self._valor - (self._valor * (percentual / 100))

	# Getter
	@property
	def valor(self):
		return self._valor

	# Setter
	@valor.setter
	def valor(self, novo_valor):
		if isinstance(novo_valor, str):
			novo_valor = float(novo_valor.replace('R$', ''))
			
		self._valor = novo_valor


# Este formato de Getter e Setter funciona junto da instancia da classe,
# sem a necessidade de serem chamados
new_product = Produto('Cerveja', 'R$50')

# chamada dos Getters que retornam as variaveis privadas
new_product.desconto(10)
print(new_product.valor)
