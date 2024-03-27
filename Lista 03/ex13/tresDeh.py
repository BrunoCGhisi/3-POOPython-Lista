from ingresso import Ingresso

class TresDeh(Ingresso):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome, disponibilidade)
        valor += 30
        self.valor = valor