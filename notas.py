1   def calcular_nota(nota1, nota2, nota3):
  1        media = (nota1 + nota2 + nota3)/3
  2        return media
  3 def exibicao_nota(nota1, nota2, nota3):
  4        media = calcular_nota (nota1, nota2, nota3)
  5        if media < 7:
  6             print("reprovado")
  7        else:
  8             print("aprovado") 
  9 if __name__ == "__main__":
 10     nota1 = float(input("Nota 1: "))
 11     nota2 = float(input("Nota 2: "))
 12     nota3 = float(input("Nota 3: "))
 13     exibicao_nota(nota1, nota2, nota3)
