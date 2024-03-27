from produto import Produto

class Revista(Produto):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome, disponibilidade)
        valor += 21
        self.valor = valor