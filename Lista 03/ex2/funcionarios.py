class Funcionarios():
    def __init__(self, cpf, nome, horas):
        self.cpf    = cpf
        self.nome   = nome
        self.horasT = horas

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, a):
        raise ValueError("Deu erro, use o método!")

    def calcularSalario(self):
        print(f"{30*'---'}Calculando salário!")
        self.__salario = self.horasT * self.valorH
        print(f"seu salário atual {self.nome} é {self.__salario}")
    
    def calcularBonus(self):
        print(f"{30*'---'}Calculando Bônus!")
        self.bonus = float(input("Qual o seu bonus a receber ?" ))
        self.__salario += self.bonus
        print(f"seu salário atual (com bonus) é {self.__salario}")