def verificacao(x, y):
    y = y - 1500
    x = (y*0.05)+x
    print(x)
def main():
    sal = float(input("Qual seu salario "))
    ven = float(input("Qual o valor de suas vendas efetuadas ?"))
    sal = (sal*0.03)+sal
    if ven >= 1500:
        verificacao(sal, ven)
main()
