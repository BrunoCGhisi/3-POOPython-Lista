class Produto:
    def __init__(self, nome, disponibilidade):
        self.nome = nome
        self.__disponibilidade = disponibilidade

    @property 
    def disponibilidade(self):
        return self.__disponibilidade
    
    @disponibilidade.setter
    def disponibilidade(self, a):
        raise ValueError("Não da de alterar a disponibilidade dessa forma!")
    
    def Reservar(self):
        x = int(input(f"Quantos {self.nome}  você vai Reservar? "))
        self.__disponibilidade -= x
        print(f"Você reservou {x} ! O número atual de {self.nome}  é {self.__disponibilidade}")

    def Devolver(self):
        x = int(input(f"Quantos {self.nome}  você vai devolver? "))
        self.__disponibilidade += x
        print(f"Você Liberou {x} ! O número atual de {self.nome}  é {self.__disponibilidade}")

    def visualizarEstoque(self):
        print(f"O número atual de {self.nome} é {self.__disponibilidade}")
        