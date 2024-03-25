class Banco():
    def __init__ (self, nome, senha, email, saldo):
        self.nome    = nome
        self.senha   = senha
        self.email   = email
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, a):
        raise ValueError("Use os métodos depositar ou debitar o valor")
    
    def sacar(self, saque):
        self.__saldo -= saque 
        print(f"Seu novo saldo: {self.__saldo}")

    def depositar(self, saque):
        self.__saldo += saque 
        print(f"Seu novo saldo: {self.__saldo}")