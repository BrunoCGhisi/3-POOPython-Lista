import random
lista = []
listaF = []
filtrados = 0
nfiltrados = 0
for i in range(8):
    lista.append(random.randint(1,100))
print(lista)

for y in lista:
    if  y < 40:
        listaF.append(y)
print(30*"---")
print("RESULTADO MAN")
print(f"{sum(listaF)}")


        
