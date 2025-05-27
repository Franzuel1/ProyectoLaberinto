import json
from laberinto_builder import LaberintoBuilder
from bicholoco import BichoLoco
from agresivo import Agresivo
from perezoso import Perezoso
from cofre import Cofre

class Director:
    def __init__(self):
        self.builder = None
        self.dict=None

    def obtenerJuego(self):
        return self.builder.obtenerJuego()
    
    def procesar(self,unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def iniBuilder(self):
        if self.dict['forma']=='cuadrado':
            self.builder=LaberintoBuilder()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each,'root')
        
        for each in self.dict['puertas']:
            # Soporta puertas normales y puertas bloqueadas (con 5 elementos y el diccionario de opciones)
            if len(each) == 5 and isinstance(each[4], dict) and "bloqueada" in each[4]:
                self.builder.fabricarPuerta(each[0], each[1], each[2], each[3], bloqueada=each[4]["bloqueada"])
            else:
                self.builder.fabricarPuerta(each[0], each[1], each[2], each[3])

    def fabricarLaberintoRecursivo(self, each, padre):
        print(each)
        if each['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(each['num'])
        if each['tipo'] == 'tunel':
            self.builder.fabricarTunelEn(padre)
        if 'hijos' in each.keys():
            for cadaUno in each['hijos']:
                if cadaUno.get("tipo") == "cofre":
                    tipo_recompensa = cadaUno.get("tipo_recompensa")
                    cantidad = cadaUno.get("cantidad")
                    cofre = Cofre(tipo=tipo_recompensa, cantidad=cantidad)
                    con.agregar_hijo(cofre)
                else:
                    self.fabricarLaberintoRecursivo(cadaUno, con)

    def leerArchivo(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict=data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def fabricarBichos(self):
        for bicho in self.dict["bichos"]:
            pos = self.builder.obtenerHabitacion(bicho["posicion"])
            if pos is None:
                continue  # Protege de errores si no se encuentra la habitación
            if bicho.get("tipo") == "bicholoco":
                nuevo_bicho = self.builder.crear_bicholoco(pos)
            else:
                modo = bicho["modo"]
                if modo == "Agresivo":
                    nuevo_bicho = self.builder.crear_bicho(3, 1, pos, Agresivo())
                elif modo == "Perezoso":
                    nuevo_bicho = self.builder.crear_bicho(3, 1, pos, Perezoso())
            self.builder.juego.agregar_ente(nuevo_bicho)
