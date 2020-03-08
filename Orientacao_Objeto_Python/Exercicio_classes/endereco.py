class Endereco:
    def __init__(self, pais, estado, cidade, bairro, rua):
        self.pais = pais
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua

    @property
    def pais(self):
        return self._pais
        
    @pais.setter
    def pais(self, pais):
        self._pais = pais
       
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado
    
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade
       
    @property
    def bairro(self):
        return self._bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro
        
    @property
    def rua(self):
        return self._rua
    
    @rua.setter
    def rua(self, rua):
        self._rua = rua

    def __str__(self):
        return f"Pais: {self.pais} \n" \
               f"Estado: {self.estado} \n" \
               f"Cidade: {self.cidade} \n" \
               f"Bairro: {self.bairro} \n" \
               f"Rua: {self.rua} \n"