import random, time
from bicho import Bicho

class BichoLoco(Bicho):
    def actua(self):
        print("BichoLoco actuando al azar.")
        while self.estaVivo():
            time.sleep(1)
            puertas = self.posicion.forma.orientaciones
            random.shuffle(puertas)
            for orientacion in puertas:
                puerta = orientacion.obtenerElemento(self.posicion.forma)
                if puerta and puerta.esPuerta():
                    destino = puerta.lado1 if puerta.lado2 == self.posicion else puerta.lado2
                    print(f"BichoLoco moviéndose a la habitación {destino.num}")
                    destino.entrar(self)
                    break

    def __str__(self):
        return "bicho-loco"
