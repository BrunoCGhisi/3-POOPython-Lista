from personagens import Personagem

class Guerreiro(Personagem):
    def __init__(self):
        super().__init__(self)
        self.vida    = 20 + self.cont
        self.dano    = 5  + self.ste
        self.esquiva = 3  + self.dx

    def ataquePesado(self):
        self.dano += 2*(self.ste)
        
