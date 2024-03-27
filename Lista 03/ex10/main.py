
from economico import Economico
from executivo import Executivo
from pClasse   import PClasse


aviao1 = Economico('aviao1', 50, 10)
aviao1.Reservar()
aviao1.Liberar()

aviao2 = Executivo('aviao2', 10, 40)
aviao2.Reservar()
aviao2.Liberar()


aviao3 = PClasse('aviao3', 50, 35)
aviao3.Reservar()
aviao3.Liberar()

