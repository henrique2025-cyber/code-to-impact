semana = int(input(print("voce commitou quantos dias hoje?")))
prova = input(print("voce teve prova hoje"))
if semana >= 5:
  print("commit todos os dias? pode jogar xadrez")
else: 
  print("não pode jogar!")
elif prova == "sim":
  print("tudo bem, voce não precisava codar")
else:
  print("ok, menos mal")
