class Item:
  def __init__(self, nome, tetoCompra, tetoVenda):
    self.nome=nome
    self.tetoCompra=tetoCompra
    self.tetoVenda=tetoVenda
  

def getItems():
  itens = []
  with open("package/entradas/armas.txt") as fp:
    for line in fp:
      nomeItem = line.rstrip()
      itens.append(Item(nomeItem, 1000000, 0))
  
  return itens


