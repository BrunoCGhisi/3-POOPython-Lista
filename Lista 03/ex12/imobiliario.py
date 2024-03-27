from investimento import Investimento

class Imobiliario(Investimento):
    def __init__(self, mestotal, dinheiro, usuario):
        super().__init__(mestotal, dinheiro)
        self.usuario = usuario