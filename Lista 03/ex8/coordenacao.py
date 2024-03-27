from integrante import Integrante

class Coordenacao(Integrante):
    def __init__(self, codigo, registro , hora_valor, hora_trabalhada):
        super().__init__(codigo, registro)
        self.hora_valor      = hora_valor
        self.hora_trabalhada = hora_trabalhada