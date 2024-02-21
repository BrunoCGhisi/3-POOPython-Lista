def calcu(x,y,z,d):
    saldo = z - y + d
    if saldo > 0:
        print(f"parabens cliente: {x} você tem o saldo positivo")
    else:
        print(f"fudeu man cliente: {x} você tem o saldo negativo :( ")

def main():
    cod = int(input("Qual seu codigo"))
    deb = float(input("QUal seu debito"))
    sald = float(input("QUal seu saldo atual"))
    cre = float(input("QUal seu credito"))
    calcu(cod, deb, sald, cre)
main()
