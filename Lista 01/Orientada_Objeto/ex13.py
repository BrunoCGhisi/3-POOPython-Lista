def verificar(x):
    x.sort()
    print(f"{x[1] + x[2]}")
    

def main():
    lista = []
    
    lista.append(int(input("Numero 1")))
    lista.append(int(input("Numero 2")))

    while lista[0] == lista[1]:
        lista.remove(1)
        lista.append(int(input("Numero 2")))
    lista.append(int(input("Numero 3")))

    while lista[2] == lista[1]:
        lista.remove(2)
        lista.append(int(input("Numero 3")))
    verificar(lista)

main()
