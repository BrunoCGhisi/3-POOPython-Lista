class Aluno():
    def __init__(self, cpf, nome, alunos):
        self.cpf = cpf
        self.nome = nome
    
    def __str__(self):
        return self.nome

class Equipe():
    def __init__(self, participantes, projeto):
        self.participantes = participantes
        self.projeto = projeto

    def __str__(self):
        participantes_nomes = ", ".join(str(aluno) for aluno in self.participantes)
        return f"Projeto: {self.projeto}, Participantes: {participantes_nomes}"

class GerenciadorEquipes():
    def __init__(self, equipes=None):
        if equipes is None:
            self.equipes = []
        else:
            self.equipes = equipes

    def CriarEquipe(self, participantes, projeto):
        for equipe in self.equipe:
            if equipe.projeto == projeto:
                for aluno in equipe.participantes:
                    if aluno in participantes:
                        return "Aqeuipe nao pode criada. "
        nova_equipe = equipe
        self.equipe.append(nova_equipe)
        return "A equipe foi criada com sucesso"

gerenciador = GerenciadorEquipes()

#cria 9 alunos

alunos = [Aluno(f"Aluno {i+1}", f"cpf {i+1}") for i in range(9)]

for i in range(3):
    particpantes = alunos[i*3:(i+1)*3]
    projeto = f"Projeto {i+3}"
    resultado = gerenciador.criarEquipe(particpantes, projeto)
    print(resultado)


for equipe in gerenciador.equipes:
    print(equipe)








