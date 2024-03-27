from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome, modelo, tipo, vm):
        super().__init__(nome, modelo)
        self.tipo = tipo
        vm += 30
        self.vm = vm