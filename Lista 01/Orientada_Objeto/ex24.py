def gasolina(x):
    if x < 20:
        y = (-3.3*0.03)+3.3
        x = (x*y)
    print(x)
    




def main():
    choice = input("Qual o tipo de combustível ? G para Gasolina /// A para Alcool")
    L = int(input("Quantos litros voce comprou ?"))
    if choice == "G":
        gasolina(L)
    

main()
