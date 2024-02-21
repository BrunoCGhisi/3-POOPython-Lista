def main():
    lista = []
    lista.append(int(input("Numero 1")))
    lista.append(int(input("Numero 2")))
    while lista[1] == 0:
        lista.remove(1)
        lista.append(int(input("Numero 2")))
    print(lista)
main()
