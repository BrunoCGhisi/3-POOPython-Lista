from produtos   import Produtos
from roupa      import Roupas
from alimento   import Alimentos

calca_jeans = Roupas(1, 'BillieJeans', 10, 40, 'calça')
calca_jeans.calcularImpostoRoupa()
calca_jeans.Comprar(2)
calca_jeans.Repor(4)

Hamburgao_Apovoro = Alimentos(2, 'Hamburgao do Apovoro', 15, 25, 'Hamburguer')
Hamburgao_Apovoro.calcularImpostoAlimento()
Hamburgao_Apovoro.Repor(20)
Hamburgao_Apovoro.Comprar(1)





