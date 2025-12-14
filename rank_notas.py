print("qual sua nota?")
nota = float(input())
if nota >= 11:
    print("nota invalida")
elif nota >= 9.5:
    print("seloko cara você é bom, hein?")
elif nota >= 8:
    print("mais ou menos tem que melhorar!")
elif nota >= 7:
    print("meu deus sem comentario")
elif nota >= 6:
    print("tem que melhorar muito cara!")
elif nota >= 0:
    print("seu burro repetiu de ano ")
else:
    print("Nota inválida. A nota não pode ser negativa.")
