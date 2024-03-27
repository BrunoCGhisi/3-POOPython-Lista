
from cd         import Cd
from hq         import Hq
from revista    import Revista


Validation = Cd('Validation - Yung Li', 55, 30)
Validation.Reservar()
Validation.Devolver()
Validation.visualizarEstoque()

Watchmen = Hq('Watchmen - Alan Moore', 100, 70)
Watchmen.Reservar()
Watchmen.Devolver()
Watchmen.visualizarEstoque()

Jornal = Revista('Jornal', 200, 10)
Jornal.Reservar()
Jornal.Devolver()
Jornal.visualizarEstoque()


