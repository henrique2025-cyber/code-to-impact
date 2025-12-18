tempo = float(input("qual é seu tempo no speedrun do super mario bros"))
if tempo >= 41.02:
    print("quase lá, faltam,", tempo - 41.02, ",segundos(ou milisegundos).")
elif tempo <= 41.02:
    print("parabéns voce bateu o recorde mundial!")
