from funcionarios import Funcionarios
from programador  import Programador
from analista     import Analista
from gerente      import Gerente

bruno = Programador(123, 'bruno', 60)
bruno.calcularSalario()

maria = Analista(456, 'maria', 90)
maria.calcularSalario()

Edinho = Gerente(789, 'Rafael', 90)
Edinho.calcularSalario()
Edinho.calcularBonus()