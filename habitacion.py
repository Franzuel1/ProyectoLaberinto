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

        # --- BOMBAS: si hay una bomba, que "explote" ---
        for hijo in getattr(self, "hijos", []):
            from bomba import Bomba
            if isinstance(hijo, Bomba):
                hijo.entrar(alguien)

        # Objetivo final: visitar todas las habitaciones
        from ente import Personaje
        if isinstance(alguien, Personaje):
            alguien.habitaciones_visitadas.add(self.num)
            total_habitaciones = len(alguien.juego.laberinto.hijos)
            print(f"Habitaciones visitadas: {sorted(alguien.habitaciones_visitadas)} / {total_habitaciones}")

            # --- PÉRDIDA: sin vidas ---
            if alguien.vidas <= 0:
                print("\n💀 ¡Te has quedado sin vidas! Has perdido la partida.")
                alguien.juego.terminarBichos()
                alguien.juego.finalizar_cronometro()
                print(f"Puntuación final: {alguien.juego.puntuacion}")
                print(f"Tiempo total: {alguien.juego.tiempo_total():.2f} segundos")
                exit(0)

            # --- PÉRDIDA: se ha acabado el tiempo ---
            if alguien.juego.tiempo_total() >= alguien.juego.tiempo_maximo:
                print("\n⏰ ¡Se ha acabado el tiempo! Has perdido la partida.")
                alguien.juego.terminarBichos()
                alguien.juego.finalizar_cronometro()
                print(f"Puntuación final: {alguien.juego.puntuacion}")
                print(f"Tiempo total: {alguien.juego.tiempo_total():.2f} segundos")
                exit(0)

            # --- Victoria: visitadas todas las habitaciones ---
            if len(alguien.habitaciones_visitadas) == total_habitaciones:
                alguien.juego.finalizar_cronometro()

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def __str__(self):
        return "Soy una habitacion"
