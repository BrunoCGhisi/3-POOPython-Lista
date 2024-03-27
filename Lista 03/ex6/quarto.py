class Quarto:
    def __init__(self, endereco, disponibilidade):
        self.endereco = endereco
        self.__disponibilidade = disponibilidade

    @property 
    def disponibilidade(self):
        return self.__disponibilidade
    
    @disponibilidade.setter
    def disponibilidade(self, a):
        raise ValueError("Não da de alterar a disponibilidade dessa forma!")
    
    def Hospedar(self):
        x = int(input("Quantos quartos você vai hospedar? "))
        self.__disponibilidade -= x
        print(f"Você reservou {x} quartos! O número atual de quartos é {self.__disponibilidade}")

    def Liberar(self):
        x = int(input("Quantos quartos você vai Liberar? "))
        self.__disponibilidade += x
        print(f"Você Liberou {x} quartos! O número atual de quartos é {self.__disponibilidade}")
        