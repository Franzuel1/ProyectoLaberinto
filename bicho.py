from modo import Modo
from agresivo import Agresivo
from ente import Ente
import time

class Bicho(Ente):
    def __init__(self):
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
            time.sleep(2) # Para evitar spam de prints
        print("Bicho termina su hilo porque vidas <= 0")

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()