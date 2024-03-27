from integrante import Integrante

class Aluno(Integrante):
    def __init__(self, codigo, registro ,n1, n2):
        super().__init__(codigo, registro)
        self.n1 = n1 
        self.n2 = n2
        