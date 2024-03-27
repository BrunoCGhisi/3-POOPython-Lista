from produto import Produto

class Cd(Produto):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome , disponibilidade)
        valor += 10
        self.valor = valor