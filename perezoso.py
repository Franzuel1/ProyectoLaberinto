import time
from modo import Modo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Perezoso: Zzzzz...")
        time.sleep(3)

    def caminar(self, bicho):
        print("Perezoso: Caminando sin ganas...")

    def atacar(self, bicho):
        print("Perezoso: ¡Atacando con furia!")
        personaje = bicho.juego.personaje if hasattr(bicho.juego, 'personaje') else None
        if personaje and bicho.posicion == personaje.posicion:
            personaje.vidas -= bicho.poder if bicho.poder is not None else 1
            print(f"⚡ El bicho PEREZOSO te ataca y pierdes {bicho.poder} vida(s). Vidas restantes: {personaje.vidas}")
        else:
            print("¡Ataque fallado!")

    def __str__(self):
        return "-perezoso"