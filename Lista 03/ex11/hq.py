from produto import Produto

class Hq(Produto):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome, disponibilidade)
        valor += 50
        self.valor = valor