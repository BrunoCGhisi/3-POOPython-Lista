class Voo:
    def __init__(self, rota, disponibilidade):
        self.rota = rota
        self.__disponibilidade = disponibilidade

    @property 
    def disponibilidade(self):
        return self.__disponibilidade
    
    @disponibilidade.setter
    def disponibilidade(self, a):
        raise ValueError("Não da de alterar a disponibilidade dessa forma!")
    
    def Reservar(self):
        x = int(input("Quantos voos você vai Reservar? "))
        self.__disponibilidade -= x
        print(f"Você reservou {x} voos! O número atual de voos é {self.__disponibilidade}")

    def Liberar(self):
        x = int(input("Quantos voos você vai Liberar? "))
        self.__disponibilidade += x
        print(f"Você Liberou {x} voos! O número atual de voos é {self.__disponibilidade}")
        