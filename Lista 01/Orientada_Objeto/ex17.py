def calculo(x):
    y = x[0] + x[1]
    y = y / 2
    print(y)

def main():
    lista = []
    lista.append(int(input("Numero 1")))
    while lista[0] < 0 or lista[0] > 10:
        lista.remove(0)
        lista.append(int(input("Numero 1")))
    lista.append(int(input("Numero 2")))
    while lista[1] < 0 or lista[1] > 10:
        lista.remove(1)
        lista.append(int(input("Numero 2")))
    calculo(lista)
    
main()
