def verificar(x):
    if x == 0:
        print("neutro")
    elif x > 0:
        print("positivo")
    elif x < 0:
        print("negativo")
def main():
    num = int(input("diz um numero ai"))
    verificar(num)
main()
