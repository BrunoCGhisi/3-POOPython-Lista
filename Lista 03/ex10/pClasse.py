from voo import Voo

class PClasse(Voo):
    def __init__(self, rota, disponibilidade, valor):
        super().__init__(rota, disponibilidade)
        valor += 500
        self.valor = valor