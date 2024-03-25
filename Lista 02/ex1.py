class Triangulo():
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    
    def calcular_perimetro(self):
        print(f'O perimetro é {self.ladoA + self.ladoB + self.ladoC}')

    def get_Maior_Lado(self):
        print(max(self.ladoA, self.ladoB, self.ladoC),"O maior lado")
    
    def calcular_Area(self):
        print(f"A Area é {(self.ladoA*self.ladoB)/2}")

a = int(input("Digite o lado A"))
b = int(input("Digite o lado B"))
c = int(input("Digite o lado C"))


meuTriangulo = Triangulo(a,b,c)
meuTriangulo.calcular_perimetroalcularPerimetro()
meuTriangulo.get_Maior_Lado()
meuTriangulo.calcular_Area()

