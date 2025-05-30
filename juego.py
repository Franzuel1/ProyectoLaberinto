import copy
from laberinto import Laberinto
from bicho import Bicho
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from agresivo import Agresivo
from perezoso import Perezoso
from pared import Pared
from bomba import Bomba
from pared_bomba import ParedBomba
from ente import Personaje
import time

class Juego:
    def __init__(self):
        self.habitaciones = {}
        self.bichos = []
        self.laberinto = None
        self.prototipo = None
        self.personaje = None
        self.bicho_threads = {}
        # CRONÓMETRO EXTRA:
        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.tiempo_maximo = 60
        # PUNTUACIÓN:
        self.puntuacion = 0

    def iniciar_cronometro(self):
        self.tiempo_inicio = time.time()

    def finalizar_cronometro(self):
        self.tiempo_fin = time.time()

    def tiempo_total(self):
        if self.tiempo_inicio is None:
            return 0
        if self.tiempo_fin is None:
            return time.time() - self.tiempo_inicio
        return self.tiempo_fin - self.tiempo_inicio
    
    def sumar_puntos(self, puntos):
        self.puntuacion += puntos
        print(f"¡Has ganado {puntos} puntos! Puntuación actual: {self.puntuacion}")

    def restar_puntos(self, puntos):
        self.puntuacion -= puntos
        print(f"Has perdido {puntos} puntos. Puntuación actual: {self.puntuacion}")


    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)
    
    def agregar_ente(self, ente):
        ente.juego = self
        self.bichos.append(ente)

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

    def lanzarBicho(self, bicho):
        import threading
        thread = threading.Thread(target=bicho.actua)
        if bicho not in self.bicho_threads:
            self.bicho_threads[bicho] = []
        self.bicho_threads[bicho].append(thread)
        thread.start()

    def terminarBicho(self, bicho):
        if bicho in self.bicho_threads:
            for thread in self.bicho_threads[bicho]:
                bicho.vidas = 0

    def lanzarBicho(self, bicho):
        import threading
        thread = threading.Thread(target=bicho.actua)
        thread.daemon = True
        if bicho not in self.bicho_threads:
            self.bicho_threads[bicho] = []
        self.bicho_threads[bicho].append(thread)
        thread.start()

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregar_personaje(self, nombre):
        self.personaje = Personaje(10, 1, self, nombre)
        self.laberinto.entrar(self.personaje)
        self.personaje.llaves = 1  # Le damos 1 llave


    def buscarPersonaje(self, bicho):
        if bicho.posicion == self.personaje.posicion:
            print(f"El bicho {bicho} ataca al personaje {self.personaje}")
            self.personaje.esAtacadoPor(bicho)


    def abrir_puertas(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                print(f"Abriendo puerta", obj)
                obj.abrir()
                self.sumar_puntos(5)  # Sumar 5 puntos por abrir puerta
        self.laberinto.recorrer(abrirPuertas)

    def abrir_puertas_con_personaje(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                print(f"Intentando abrir puerta", obj)
                print(f"El personaje tiene {self.personaje.llaves} llaves antes de intentar abrir.")
                if obj.bloqueada:
                    if self.personaje.llaves > 0:
                        obj.abrir(tiene_llave=True)
                        self.personaje.llaves -= 1
                        print("¡Has usado una llave! Llaves restantes:", self.personaje.llaves)
                    else:
                        obj.abrir(tiene_llave=False)
                else:
                    obj.abrir()
                self.sumar_puntos(5) # Sumar 5 puntos por abrir puerta
        self.laberinto.recorrer(abrirPuertas)

    def cerrar_puertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                print(f"Cerrando puerta", obj)
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto
    
    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.ponerElementoEnOrientacion(puerta, Norte())
        habitacion2.ponerElementoEnOrientacion(puerta, Sur())
        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.ponerElementoEnOrientacion(bomba1, Este())
        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.ponerElementoEnOrientacion(bomba2, Oeste())
        laberinto.agregarHabitacion(habitacion1)
        laberinto.agregarHabitacion(habitacion2)
        return laberinto

    def crearLaberinto4Hab(self, creator):
        laberinto = creator.crear_laberinto()
        habs = [creator.crear_habitacion(i) for i in range(1, 5)]
        puertas = [
            creator.crear_puerta(habs[0], habs[1]),
            creator.crear_puerta(habs[0], habs[2]),
            creator.crear_puerta(habs[1], habs[3]),
            creator.crear_puerta(habs[2], habs[3])
        ]
        habs[0].ponerElementoEnOrientacion(puertas[0], Sur())
        habs[0].ponerElementoEnOrientacion(puertas[1], Este())
        habs[2].ponerElementoEnOrientacion(puertas[1], Oeste())
        habs[2].ponerElementoEnOrientacion(puertas[3], Sur())
        habs[1].ponerElementoEnOrientacion(puertas[0], Norte())
        habs[1].ponerElementoEnOrientacion(puertas[2], Este())
        habs[3].ponerElementoEnOrientacion(puertas[3], Norte())
        habs[3].ponerElementoEnOrientacion(puertas[2], Oeste())
        for h in habs:
            laberinto.agregarHabitacion(h)
        return laberinto

    def terminarJuego(self):
        Juego.finalizar_cronometro()
        self.terminarBichos()
