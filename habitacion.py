from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"--- ENTRANDO en la habitación {self.num} ---")
        alguien.posicion = self
        # -- Cofres SOLO el personaje los abre --
        if hasattr(self, "hijos") and type(alguien).__name__ == "Personaje":
            for hijo in self.hijos:
                from cofre import Cofre
                if isinstance(hijo, Cofre):
                    hijo.abrir(alguien, alguien.juego)
        # Objetivo final: visitar todas las habitaciones
        from ente import Personaje
        if isinstance(alguien, Personaje):
            alguien.habitaciones_visitadas.add(self.num)
            total_habitaciones = len(alguien.juego.laberinto.hijos)
            print(f"Habitaciones visitadas: {sorted(alguien.habitaciones_visitadas)} / {total_habitaciones}")
            if len(alguien.habitaciones_visitadas) == total_habitaciones:
                alguien.juego.finalizar_cronometro()

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
    def calcularPosicion(self):
        self.forma.calcularPosicion()
    def __str__(self):
        return "Soy una habitacion"
