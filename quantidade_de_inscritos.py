inscritos = int(input("quantas pessoas fazem parte da comunidade de inscritos do seu canal:"))
dias = int(input("quantos dias terá a simulação:"))
porcentagem = int(input("qual será a porcentagem da taxa de crescimento:"))
final = inscritos * ( (1+(porcentagem/100)) ** dias)
print("Depois da simulacao:")
print("Inscritos:", int(final))
if final >= 100000:
    print("PLACA DE PRATA!")
else:
    print("Ainda nao chegou na placa.")
