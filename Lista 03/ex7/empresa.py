from conta import Conta

class Empresa(Conta):
    def __init__(self, nome, senha, email, logo_marca, conta_corrente):
        super().__init__(nome, senha, email)
        self.logo_marca = logo_marca
        self.conta_corrente = conta_corrente
        