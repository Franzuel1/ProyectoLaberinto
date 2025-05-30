import time
from modo import Modo
import random
from ente import Ente
from agresivo import Agresivo
from perezoso import Perezoso

class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.vidas > 0:
            if self.modo:
                self.modo.actuar(self)
            else:
                print("Bicho haciendo cosas...")
            self.mover_aleatorio()  # Después de actuar, se mueve y ataca si toca
            time.sleep(2)
        print("Bicho termina su hilo porque vidas <= 0")

    def mover_aleatorio(self):
        if not self.juego or not self.juego.personaje:
            return
        destino = self.juego.personaje.posicion
        if destino != self.posicion:
            # Se muece a la habitación del personaje (forzar para probar)
            print(f"{self} se mueve a la habitación del personaje {destino.num}")
            destino.entrar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un bicho" + self.modo.__str__()