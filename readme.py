print('quanto voce tirou na prova?')
nota = float(input())
if nota < 0 or nota > 10:
    print('nota invalida')
elif nota >= 9.5:
    print('que isso, lenda!')
elif nota >= 8:
    print('quase mas esta bom mesmo assim')
elif nota >= 7:
    print('tem que melhorar muito')
elif nota >= 4:
    print('ficou de re-cu-pe-ra-cao')
else:
    print('vai fazer kumon cara, voce nao leva jeito')
