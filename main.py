from juego import Juego
from creator import CreatorBasico

def main():
    print("¡Bienvenido al juego del Laberinto!")

    # Crear un creador de laberinto (puedes cambiarlo a otro tipo de Creator)
    creador = CreatorBasico()

    # Inicializar el juego con el creador
    juego = Juego(creador)

    # Iniciar y jugar
    juego.iniciar_juego()
    juego.jugar()

if __name__ == "__main__":
    main()
