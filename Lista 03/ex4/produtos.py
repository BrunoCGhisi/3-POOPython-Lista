class Produtos:
    def __init__(self,codigo,nome,quantidade):
        self.codigo = codigo
        self.nome   = nome
        self.__qntd   = quantidade
    
    @property
    def qntd(self):
        return self.__qntd
    @qntd.setter
    def qntd(self,a):
        raise ValueError("Você não pode só pegar um valor de fora! Altere pelos métodos!!!")
    
    def calcularImpostoRoupa(self):
        print(f"{10*'---'}Calculando Imposto sobre Roupa{10*'---'}")
        self.valor += (self.valor * 0.5)
        print(f"{10*'---'} O preco atual do {self.nome} é {self.valor} {10*'---'}")
        print(f"{30*'---'}")

    def calcularImpostoAlimento(self):
        print(f"{10*'---'}Calculando Imposto sobre Alimento{10*'---'}")
        self.valor += (self.valor * 0.25)
        print(f"{10*'---'} O preco atual do {self.nome} é {self.valor} {5*'---'}")
        print(f"{30*'---'}")

    def Comprar(self, x):
        print(f"{10*'---'}Você Coprou: {x} do estoque {10*'---'}")
        self.__qntd -= x
        print(f"{10*'---'} Atualmente temos {self.__qntd} de {self.nome} {5*'---'}")
        print(f"{30*'---'}")
    
    def Repor(self, y):
        print(f"{10*'---'}Você Coprou: {y} do estoque {10*'---'}")
        self.__qntd += y
        print(f"{10*'---'} Atualmente temos {self.__qntd} de {self.nome} {5*'---'}")
        print(f"{30*'---'}")

    