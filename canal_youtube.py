inscritos = int(input(print('olá, quantos inscritos tem seu canal no youtube?')))
dias = int(input(print("ótimo, agora me fale quantos dias voce quer que tenha a sua simulacao?")))
total = inscritos * 1.5
if total <= 100000:
    print("voce tem a placa de prata!")
elif total <= 100000:
    print("voce tem a placa de ouro!")
elif total <= 10000000:
    print("meu deus! 10 milhões!")
elif total <= 100000000:
    print("impossivel! wow!")
else:
    print("poste mais videos,amigo!")
