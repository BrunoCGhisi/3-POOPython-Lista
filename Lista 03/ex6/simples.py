from quarto import Quarto

class Simples(Quarto):
    def __init__(self, endereco, disponibilidade, valor):
        super().__init__( endereco, disponibilidade)
        valor += 20
        self.valor = valor
