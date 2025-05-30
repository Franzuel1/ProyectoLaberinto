import time
from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo: Durmiendo un poco...")
        time.sleep(1)

    def caminar(self, bicho):
        print("Agresivo: Caminando con determinación...")

    def atacar(self, bicho):
        print("Agresivo: ¡Atacando con furia!")
        personaje = bicho.juego.personaje if hasattr(bicho.juego, 'personaje') else None
        if personaje and bicho.posicion == personaje.posicion:
            personaje.vidas -= bicho.poder if bicho.poder is not None else 1
            print(f"⚡ El bicho AGRESIVO te ataca y pierdes {bicho.poder} vida(s). Vidas restantes: {personaje.vidas}")
        else:
            print("¡Ataque fallado!")


    def __str__(self):
        return "-agresivo"