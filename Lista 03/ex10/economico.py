from voo import Voo

class Economico(Voo):
    def __init__(self, rota, disponibilidade, valor):
        super().__init__( rota, disponibilidade)
        valor += 200
        self.valor = valor
