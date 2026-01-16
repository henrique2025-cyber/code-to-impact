print("~~~~MEDIDOR DE OVERALL DO HEROÍ~~~~")
nome = input(print("qual o nome do seu heroi?  "))
força = int(input(print("qual é a força do seu heroi? 0 a 10 ")))
poder = int(input(print("seu super-heroi é poderoso? 0 a 10 ")))
inteligencia = int(input(print("qual é a mentalidade do seu heroi? 0 a 10 ")))
coragem = int(input(print("seu heroi é corajoso? 0 a 10 ")))
sagacidade = int(input(print("qual é a sagacidade do seu heroi? 0 a 10 ")))
overall = (força + poder + inteligencia + coragem +sagacidade) * 2 
print("o ",nome," tem um overall de",overall,".")
if overall > 100:
    print("tente novamente, error 404")
