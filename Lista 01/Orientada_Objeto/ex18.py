def calculo(x):
    y = x[0] + x[1]
    y = y / 2
    print(y)

def questionario(lista):
    while True:
        choice = int(input("Quer continuar ? 1 - Sim / 2 - Não"))
        if choice == 1:
            calculo(lista)
        elif choice == 2:
            break
        else:
            print("Escolha errada")


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
    questionario(calculo)
main()
