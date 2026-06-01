1   def converter_dolar(valor): 
  1     total = valor * 0.20
  2     return total
  3 def converter_euro(valor):
  4     total = valor * 0.18
  5     return total
  6 def exibir_valor(valor):
  7     dolar = converter_dolar(valor)
  8     euro = converter_euro(valor)
  9     print(f"Dólares: {dolar}")
 10     print(f"Euros: {euro}")
 11 if __name__ == "__main__":
 12     valor = float(input("Valor em reais: "))
 13     exibir_valor(valor) 
