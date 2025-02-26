from abc import ABC, abstractmethod
from juego import Habitacion, Bomba, BichoPerezoso, BichoAgresivo

class Creator(ABC):
    @abstractmethod
    def crear_laberinto(self):
        pass

class CreatorBasico(Creator):
    def crear_laberinto(self):
        # Crear las habitaciones
        habitacion1 = Habitacion("Habitación 1")
        habitacion2 = Habitacion("Habitación 2")

        # Conectar habitaciones
        habitacion1.establecer_conexion("norte", habitacion2)
        habitacion2.establecer_conexion("sur", habitacion1)

        # Añadir elementos a las habitaciones
        habitacion1.agregar_elemento(Bomba())
        habitacion2.agregar_elemento(BichoPerezoso())

        return habitacion1

class CreatorAvanzado(Creator):
    def crear_laberinto(self):
        # Crear más habitaciones
        habitacion1 = Habitacion("Entrada")
        habitacion2 = Habitacion("Pasillo")
        habitacion3 = Habitacion("Sala de tesoro")

        # Conectar habitaciones
        habitacion1.establecer_conexion("este", habitacion2)
        habitacion2.establecer_conexion("oeste", habitacion1)
        habitacion2.establecer_conexion("norte", habitacion3)
        habitacion3.establecer_conexion("sur", habitacion2)

        # Añadir elementos variados
        habitacion1.agregar_elemento(BichoPerezoso())
        habitacion2.agregar_elemento(Bomba())
        habitacion3.agregar_elemento(BichoAgresivo())

        return habitacion1
