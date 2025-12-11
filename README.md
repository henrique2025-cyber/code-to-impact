anos = int(input("Quantos anos você tem? "))
meses = int(input("Quantos meses além dos anos você tem? "))
dias = int(input("Quantos dias além dos meses você tem? "))

idade = anos * 365 + meses * 30 + dias

print("Você tem", idade, "dias de vida.")
