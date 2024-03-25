class Funcionario():
    def __init__(self, nome, sal):
        self.nome = nome
        self.salario = sal

    def aumentarSalario(self, x):
        self.salario += self.salario * (x/100)
        print(self.salario)

funcionario_harry = Funcionario('Harry', 2500)
print(funcionario_harry.salario)
funcionario_harry.aumentarSalario(10)