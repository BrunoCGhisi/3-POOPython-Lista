class Alunos():
    def __init__(self, nome, a):
        self.nome = nome 
        self.n1 = a
    def printar(self):
        print(f"meu nome é {self.nome}")

aluno1 = Alunos('bruno', 1)
aluno1.printar()
    