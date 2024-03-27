from voo import Voo

class Executivo(Voo):
    def __init__(self, rota, disponibilidade, valor):
        super().__init__( rota, disponibilidade)
        valor += 210
        self.valor = valor