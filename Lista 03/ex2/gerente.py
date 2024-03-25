from funcionarios import Funcionarios

class Gerente(Funcionarios):
    def __init__(self, cpf, nome, horasT):
        super().__init__(cpf, nome, horasT)
        self.valorH = 50
        self.bonus  = 0