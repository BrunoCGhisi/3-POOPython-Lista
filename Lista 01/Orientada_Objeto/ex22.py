import random
lista = []
filtrados = 0
nfiltrados = 0
for i in range(10):
    lista.append(random.randint(1,20))
print(lista)

for y in lista:
    if 10 < y < 20:
        filtrados+=1
    elif y < 9:
        nfiltrados+=1
print(f"O total de valores entre 10 e 20 é {filtrados} e o resto é {nfiltrados}")
