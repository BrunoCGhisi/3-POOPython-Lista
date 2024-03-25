from funcionarios import Funcionarios

class Programador(Funcionarios):
    def __init__(self, cpf, nome, horasT):
        super().__init__(cpf, nome, horasT)
        self.valorH = 20
        self.bonus  = 0 