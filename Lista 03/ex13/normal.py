from ingresso import Ingresso

class Normal(Ingresso):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome , disponibilidade)
        valor += 20
        self.valor = valor