class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.gasolina = 0

    def andar(self, distancia):
        self.gasolina =  distancia / self.consumo 

    def obterGasolina(self, gasolina):
        self.gasolina += gasolina

fusquinha = Carro(0.5)
while True:
    print(fusquinha.__dict__)
    opcao = int(input("Quer andar, encher ou sair ? 1 - andar | 2 - encher | 3 - sair "))
    if opcao == 1:
        distancia = int(input("Quanto voce andou KMs agora "))
        fusquinha.andar(distancia)
    elif opcao == 2:
        gasolina = int(input("Quanto tempo você ecnheu de gasolina Litros agora "))
        fusquinha.obterGasolina(gasolina)
    elif opcao == 3:
        break
    else:
        print(" por favor insira um valor valido ")