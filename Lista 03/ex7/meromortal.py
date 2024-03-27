from conta import Conta

class Meromortal(Conta):
    def __init__(self, nome, senha, email, foto_perfil):
        super().__init__(nome, senha, email)
        self.foto_perfil = foto_perfil
