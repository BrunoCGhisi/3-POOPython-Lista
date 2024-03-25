from produtos import Produtos

class Alimentos(Produtos):
    def __init__(self, codigo, nome, quantidade, valor_base, tipo):
        super().__init__(codigo, nome, quantidade)
        valor_base += 10
        self.valor = valor_base
        self.tipo  = tipo