import random

class Cofre:
    def __init__(self, tipo=None, cantidad=None):
        self.tipo = tipo or random.choice(["puntos", "llaves"])
        if cantidad is not None:
            self.cantidad = cantidad
        else:
            self.cantidad = random.randint(5, 20) if self.tipo == "puntos" else random.randint(1, 3)
        self.abierto = False

    def abrir(self, personaje, juego):
        # Solo los personajes (no bichos) pueden abrir cofres
        from ente import Personaje
        if not isinstance(personaje, Personaje):
            # Si no es el jugador, ignoramos el cofre
            return

        if self.abierto:
            print("Este cofre ya se abrió antes.")
            return
        self.abierto = True
        if self.tipo == "puntos":
            juego.sumar_puntos(self.cantidad)
            print(f"¡Has encontrado un cofre con {self.cantidad} puntos!")
        elif self.tipo == "llaves":
            personaje.llaves += self.cantidad
            print(f"¡Has encontrado un cofre con {self.cantidad} llave(s)!")

    def recorrer(self, func):
        func(self)

    def __str__(self):
        return f"Soy un cofre de {self.tipo} con {self.cantidad}"
