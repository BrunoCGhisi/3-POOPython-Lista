from ingresso import Ingresso

class Vip(Ingresso):
    def __init__(self, nome, disponibilidade, valor):
        super().__init__( nome, disponibilidade)
        valor += 50
        self.valor = valor