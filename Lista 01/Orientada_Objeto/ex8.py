def verificar(x, y):
    verificacao = x - y
    if verificacao > (x-16):
        print("Não pode votar")
    else:
        print("pode votar")

def main():
    atual = int(input("Em que ano estamos ? "))
    idade = int(input("Qual a sua idade ? "))
    verificar(atual, idade)

main()
