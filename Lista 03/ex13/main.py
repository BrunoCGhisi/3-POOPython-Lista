
from normal     import Normal
from tresDeh    import TresDeh
from vip        import Vip


ClubedaLuta = Normal('ClubedaLuta', 30, 10)
ClubedaLuta.Reservar()
ClubedaLuta.Devolver()
ClubedaLuta.verIngressosTotal()

Barbie = TresDeh('Barbie', 30, 10)
Barbie.Reservar()
Barbie.Devolver()
Barbie.verIngressosTotal()

Openheimer = Vip('Openheimer', 15, 10)
Openheimer.Reservar()
Openheimer.Devolver()
Openheimer.verIngressosTotal()


