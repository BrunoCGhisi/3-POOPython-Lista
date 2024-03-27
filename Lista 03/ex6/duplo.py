from quarto import Quarto

class Duplo(Quarto):
    def __init__(self, endereco, disponibilidade, valor):
        super().__init__( endereco, disponibilidade)
        valor += 40
        self.valor = valor