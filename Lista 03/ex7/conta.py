class Conta:
    def __init__(self, nome, senha, email):
        self.nome    = nome
        self.__senha = senha
        self.email   = email
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.getter 
    def senha(self, a):
        raise ValueError("Não da de alterar a senha dessa forma!")
    
    def alterarSenha(self):
        senha = input("Qual a sua nova senha?")
        self.__senha = senha
        print(f"Sua nova senha {self.nome} é {self.__senha}")
    
    def postar(self):
        post = input("Qual o seu posto?")
        print(f"{self.nome} postou : '{post}' ")

    