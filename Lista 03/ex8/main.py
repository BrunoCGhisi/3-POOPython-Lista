from aluno import Aluno
from professor import Professor
from coordenacao import Coordenacao

Bruno = Aluno(1, 'Bruno', 5, 9)
Bruno.calcularMedia()

Belone = Professor(2, 'Belone', 10, 99999)
Belone.CalcularSalario

Albertina = Coordenacao(3, 'Albertina', 40, 29)
Albertina.alterarRegistro()
Albertina.CalcularSalario()