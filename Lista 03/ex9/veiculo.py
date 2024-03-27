class Veiculo:
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo

    def calcularRotar(self):
        distancia = float(input(f"Quantos KMs você vai aindar? seu carro anda {self.vm} por hora "))
        quanto_tempo = distancia/self.vm
        print(F"Você vai demorar {quanto_tempo} horas para chegar ao seu destino ")
        quanto_tempo *= 60
        print(F"Você vai demorar {quanto_tempo} minutos para chegar ao seu destino ")


