from animal import Animal

class Planta(Animal):
    def __ini__(self, nome, reproducao, alimentacao, qntd, reino, especie):
       super().__init__(nome, reproducao, alimentacao, qntd)
       self.reino   = reino
       self.especie = especie
       