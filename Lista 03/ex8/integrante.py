class Integrante:
    def __init__(self, codigo, registro):
        self.codigo  = codigo
        self.__registro = registro
    
    @property
    def senha(self):
        return self.__registro
    
    @senha.getter 
    def senha(self, a):
        raise ValueError("Não da de o resgistro dessa forma!")
    
    def alterarRegistro(self):
        registro = input("Qual o seu novo registro?")
        self.__registro = registro
        print(f" {self.__registro} seu novo registro é {self.__registro}")
    
    def calcularMedia(self):
        media = (self.n1 + self.n2)/2
        print(f"A média do {self.__registro} é {media}")
    
    def CalcularSalario(self):
        salario = self.hora_valor * self.hora_trabalhada
        print(f"O salario do {self.__registro} é {salario}")

    def ComunicarAlunos(self):
        comunicado = input("Qual o comunicado da coordenação?")
        print(f"{self.__registro} falou para todos os alunos: 'Atenção alunos e alunas {comunicado}' ")