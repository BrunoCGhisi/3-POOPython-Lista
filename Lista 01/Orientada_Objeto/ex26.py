def calculo(x):
    y = int(input("Qual a sua média de acertos ? "))
    z = (x[0] + x[1] * 2 + x[2] * 3 + y)/7
    if z <= 9.1:
        print("Aluno nota D")
    elif z >= 7.6 and z <=9:
        print("Aluno nota C")
    elif z >= 6 and z<7.5:
        print("Aluno nota B")
    elif z <= 5.9:
        print("Aluno nota A")



def main():
    notas = []
    notas.append(float(input("Qual a sua nota ? ")))
    notas.append(float(input("Qual a sua nota ? ")))
    notas.append(float(input("Qual a sua nota ? ")))
    calculo(notas)
main()
