from quarto import Quarto

class Triplo(Quarto):
    def __init__(self, endereco, disponibilidade, valor):
        super().__init__(endereco, disponibilidade)
        valor += 60
        self.valor = valor