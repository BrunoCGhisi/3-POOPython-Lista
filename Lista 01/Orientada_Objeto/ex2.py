nulo = 0
branco = 0
votou = 0
num = int(input("Qual o numero de eleitores? "))
for i in range(num):
    voto = int(input("""Qual seu tipo de voto ?
            1 - Nulo
            2 - Branco
            3 - Voto """))
    if voto == 1:
        nulo += 1
    elif voto == 2:
        branco += 1
    elif voto == 3:
        votou += 1
    else:
        branco += 1

totalN = (nulo*100)/num
totalB = (branco*100)/num
totalV = (votou*100)/num
print(f"Total de votos nulos: %{totalN}\nTotal de votos brancos: %{totalB}\nTotal de votos veridicos: %{totalV} ")
        
