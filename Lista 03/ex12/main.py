from imobiliario import Imobiliario
from titulo     import Titulo
from acao        import Acao


ClubedaLuta = Imobiliario('ClubedaLuta', 30, 10)
ClubedaLuta.Reservar()
ClubedaLuta.Devolver()
ClubedaLuta.verIngressosTotal()


Barbie = Titulo('Barbie', 30, 10)
Barbie.Reservar()
Barbie.Devolver()
Barbie.verIngressosTotal()

Openheimer = Acao('Openheimer', 15, 10)
Openheimer.Reservar()
Openheimer.Devolver()
Openheimer.verIngressosTotal()