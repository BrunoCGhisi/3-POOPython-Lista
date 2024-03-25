class Aluno:
    def __init__ (self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.totalsono = tempoSemDormir
    def estudar (self, estudo):
        
        self.totalsono -= estudo
    def dormir (self, dormir):
        self.totalsono += dormir

Bruno = Aluno('Bruno', 'Informatica', 0)
while True:
    print(Bruno.__dict__)
    opcao = int(input("Quer dormir, estudar ou sair ? 1 - dormir | 2 - estudar | 3 - sair "))
    if opcao == 1:
        dormir = int(input("Quanto tempo você dormiu agora "))
        Bruno.dormir(dormir)
    elif opcao == 2:
        estudo = int(input("Quanto tempo você estudou agora "))
        Bruno.estudar()
    elif opcao == 3:
        break
    else:
        print(" por favor insira um valor valido ")
