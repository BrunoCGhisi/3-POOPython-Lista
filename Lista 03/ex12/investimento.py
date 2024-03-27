class Investimento:
    def __init__(self, mestotal, dinheiro):
        self.meses = mestotal
        self.__dinheiro = dinheiro
    
    @property
    def dinheiro(self):
        return self.__dinheiro
    @dinheiro.setter
    def __dinheiro(self, a):
        raise ValueError("Nao da de sacar dessa forma!")
    
    def Sacar(self):
        x = input(f"{self.usuario} você tem {self.dinheiro} em sua conta atualmente, quanto deseja sacar? ")
        self.__dinheiro -= x
    
    def Investir(self):
        x = input(f"{self.usuario} você tem {self.dinheiro} em sua conta atualmente, quanto deseja investir? ")
        self.__dinheiro += x

    def InvestimentoImobiliario(self): 
        self.__dinheiro *= (self.meses*1.1)
        print(f"Senhor(a) {self.usuario} investiu durante ")

    def InvestimentoTitular(self): 
        self.__dinheiro *= (self.meses*1.5)

    def InvestimentoAcao(self): 
        self.__dinheiro *= (self.meses*2)