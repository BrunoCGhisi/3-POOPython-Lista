from veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, nome, modelo, tipo, vm):
        super().__init__(nome, modelo)
        self.tipo = tipo
        vm += 5
        self.vm = vm
