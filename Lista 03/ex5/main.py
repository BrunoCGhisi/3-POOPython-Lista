from animal     import Animal
from bacteria   import Bacteria
from humano     import Humano
from planta     import Planta

flago = Bacteria('flago', 'asexuada', 'nada', 300, 'monera', 'dofjfd')
flago.reproduzirBacteria()

Bruno = Humano('Bruno', 'sexuado', 'Tudo fi', 1, 'Animalia', 'Homo-Erectus')
Bruno.reproduzirHumano()

Girassol = Planta('Solzinhofofo', 'asexuada', 'Fotosintese', 500, 'Plantae', 'Girassolis Pralis')
flago.reproduzirPlanta()