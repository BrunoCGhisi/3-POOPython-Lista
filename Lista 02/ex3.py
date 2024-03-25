class Livro():
    def __init__(self, nome, qtdpaginas, autor, preco):
        self.nome = nome
        self.qtd = qtdpaginas
        self.autor = autor
        self.preco = preco

    def getpreco(self):
        print(f"o valor do livro é {self.preco}")

    def setpreco(self):
        self.preco = float(input("o novo preco é "))


terrorizante = Livro('terrorizante', 125, 'Clovis Coelho', 50)
terrorizante.getpreco()

while True:
    opcao = int(input("Quer alterar o preco ? 1 - sim 2 - nao"))
    print(terrorizante.__dict__)
    if opcao == 1:
        terrorizante.setpreco()
        terrorizante.getpreco()
    elif opcao == 2:
        break
    else:
        print("por favor insira um valor valido")


