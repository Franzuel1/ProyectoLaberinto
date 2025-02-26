from creator import Creator

class Juego:
    def __init__(self, creator):
        if not isinstance(creator, Creator):
            raise TypeError("El parámetro 'creator' debe ser una instancia de la clase Creator")
        self.creator = creator
        self.laberinto = None

    def iniciar_juego(self):
        print("Iniciando el juego del laberinto...")
        self.laberinto = self.creator.crear_laberinto()

    def jugar(self):
        if not self.laberinto:
            print("¡Primero debes iniciar el juego!")
            return

        print("¡Bienvenido al laberinto!")
        jugador = self.laberinto.obtener_jugador()

        while not jugador.ha_ganado():
            print("\nUbicación actual:", jugador.ubicacion)
            print("Salidas disponibles:", jugador.ubicacion.obtener_salidas())

            movimiento = input("¿A dónde quieres ir? (N/S/E/O): ").strip().upper()

            if movimiento in ["N", "S", "E", "O"]:
                jugador.mover(movimiento)
            else:
                print("Movimiento no válido. Usa N, S, E, O.")

            if jugador.esta_muerto():
                print("¡Has muerto! Fin del juego.")
                return

        print("¡Felicidades! Has salido del laberinto.")

if __name__ == "__main__":
    from creator import CreatorBasico
    juego = Juego(CreatorBasico())
    juego.iniciar_juego()
    juego.jugar()
