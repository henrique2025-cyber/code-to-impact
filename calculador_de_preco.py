1   def calcular_total(preco, quantidade):
  1     total = preco * quantidade
  2     return total
  3 
  4 def exibir_compra(produto, preco, quantidade):
  5     total = calcular_total(preco, quantidade)
  6     print(f"{produto} x{quantidade} = R$ {total}")
  7 if __name__ == "__main__":
  8     produto = (input("qual e o produto: "))
  9     quantidade = float(input("qual a quantidade: "))
 10     preco = float(input("qual e o preco: "))
 11     exibir_compra(produto, preco, quantidade)
