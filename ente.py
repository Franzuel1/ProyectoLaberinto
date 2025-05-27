class Ente:
    def __init__(self):
        super().__init__()
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.llaves = 0

    def clonarLaberinto(self,tunel):
        pass

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.vidas = vidas
        self.poder = poder
        self.juego = juego
        self.nombre = nombre
        self.llaves = 1 # Le damos 1 llave


    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()