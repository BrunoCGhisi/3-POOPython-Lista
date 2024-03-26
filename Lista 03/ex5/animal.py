class Animal:
    def __init__(self, nome, reproducao, alimentacao, qntd):
        self.nome       = nome
        self.reproducao = reproducao
        self.alimentacao= alimentacao
        self.__qntd     = qntd

    @property
    def qntd(self):
        return self.__qntd
    @qntd.setter
    def qntd(self,a):
        raise ValueError("Não da de alterar a quantidade dessa forma")
    
    def reproduzirHumano(self):
        self.__qntd += 1
        print(f"O {self.nome} se reproduziu, agora existem {self.__qntd} de {self.especie} ")

    def reproduzirBacteria(self):
        self.__qntd **= 2
        print(f"O {self.nome} se reproduziu, agora existem {self.__qntd} de {self.especie} ")

    def reproduzirPlanta(self):
        self.__qntd *= 2
        print(f"O {self.nome} se reproduziu, agora existem {self.__qntd} de {self.especie} ")