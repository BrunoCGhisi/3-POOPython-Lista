from funcionarios import Funcionarios

class Analista(Funcionarios):
    def __init__(self, cpf, nome, horasT):
        super().__init__(cpf, nome, horasT)
        self.valorH = 35
        self.bonus  = 0