class Animal:
    def __init__(self, nome, reproducao, alimentacao):
        self.nome = nome
        self.reproducao = reproducao
        self.alimentacao = alimentacao

    @property
    def qntd(self):
        return self.__qntd
    @qntd.setter
    def qntd(self,a):
        raise ValueError("Não da de alterar a quantidade")