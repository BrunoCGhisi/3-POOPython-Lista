class Ingresso:
    def __init__(self, nome_filme, disponibilidade):
        self.nome_filme = nome_filme
        self.__disponibilidade = disponibilidade

    @property 
    def disponibilidade(self):
        return self.__disponibilidade
    
    @disponibilidade.setter
    def disponibilidade(self, a):
        raise ValueError("Não da de alterar a disponibilidade dessa forma!")
    
    def Reservar(self):
        x = int(input(f"Quantos ingressos  de {self.nome_filme}  você vai Reservar? "))
        self.__disponibilidade -= x
        print(f"Você reservou {x} ! O número atual de ingressos pro {self.nome_filme}  é {self.__disponibilidade}")

    def Devolver(self):
        x = int(input(f"Quantos ingressos de {self.nome_filme}  você vai Devolver? "))
        self.__disponibilidade += x
        print(f"Você Liberou {x} ! O número atual de ingressos pro {self.nome_filme}  é {self.__disponibilidade}")

    def verIngressosTotal(self):
        print(f"O número atual de ingressos pro {self.nome_filme} é {self.__disponibilidade}")
