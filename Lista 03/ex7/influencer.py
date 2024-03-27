from conta import Conta

class Influencer(Conta):
    def __init__(self, nome, senha, email, foto_perfil, fama):
        super().__init__(nome, senha, email)
        self.foto_perfil = foto_perfil
        fama += 100000
        self.fama = fama

