class Criptomoeda:

  def __init__(self, nome, simbolo, preco, capitalizacao_de_mercado):

    self.nome = nome
    self.simbolo = simbolo
    self.preco = preco
    self.capitalizacao_de_mercado = capitalizacao_de_mercado

def calcular_variacao_de_preco(self, preco_anterior):

    if preco_anterior is None:
        return None
    
    return (self.preco - preco_anterior) / preco_anterior * 100
    
def calcular_volume_de_negociacao(self):

    return self.capitalizacao_de_mercado / self.preco
