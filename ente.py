class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.llaves = 0

    def clonarLaberinto(self, tunel):
        pass

    def recibir_daño(self, cantidad):
        self.vidas -= cantidad
        print(f"¡Has recibido {cantidad} de daño! Vidas restantes: {self.vidas}")
        # Si es el personaje y se queda sin vidas, terminar la partida
        if hasattr(self, "juego") and self.juego is not None and hasattr(self, "nombre"):
            if self.vidas <= 0:
                print("\n💀 ¡Te has quedado sin vidas! Has perdido la partida.")
                self.juego.terminarBichos()
                self.juego.finalizar_cronometro()
                print(f"Puntuación final: {self.juego.puntuacion}")
                print(f"Tiempo total: {self.juego.tiempo_total():.2f} segundos")
                exit(0)

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.vidas = vidas
        self.poder = poder
        self.juego = juego
        self.nombre = nombre
        self.llaves = 1  # Le damos 1 llave
        self.habitaciones_visitadas = set()  # Para llevar un registro de las habitaciones visitadas

    def clonarLaberinto(self, tunel):
        tunel.puedeClonarLaberinto()

    def esAtacadoPor(self, bicho):
        self.recibir_daño(bicho.poder if bicho.poder is not None else 1)