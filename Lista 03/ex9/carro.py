from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, modelo, tipo, vm):
        super().__init__(nome, modelo)
        self.tipo = tipo
        vm += 20
        self.vm = vm

        