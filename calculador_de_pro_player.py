print("CALCULADOR DE PRO PLAYER")
xp_atual = int(input("XP atual: "))
xp_por_vitoria = int(input("XP por vitória: "))
xp_necessario = int(input("XP necessário para o nível desejado: "))
falta = xp_necessario - xp_atual
if falta < 0:
    falta = 0
vitorias = 0
while vitorias * xp_por_vitoria < falta:
    vitorias = vitorias + 1
print("Você precisa ganhar", vitorias, "vitória(s).")
