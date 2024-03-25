from produtos import Produtos

class Roupas(Produtos):
    def __init__(self, codigo, nome, quantidade, valor_base, tipo):
        super().__init__(codigo, nome, quantidade)
        valor_base += 20
        self.valor = valor_base
        self.tipo  = tipo