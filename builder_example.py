from director import Director
import time

director = Director()
filename = "./laberintos/laberinto_bicholoco.json"

data = director.leerArchivo(filename)
if data:
    print("Datos cargados del JSON:")
    print(data)
else:
    print("Error al cargar JSON.")

director.procesar(filename)
juego = director.obtenerJuego()

# 1.CREA EL PERSONAJE ANTES DE ABRIR PUERTAS
juego.agregar_personaje("Jugador")

# Ejemplo de recorrido del laberinto
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

# Mostrar los bichos del juego (debe aparecer aquí el BichoLoco)
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")

# 2.ABRIR PUERTAS USANDO EL PERSONAJE (gestiona llaves)
juego.abrir_puertas_con_personaje()

juego.lanzarBichos()
time.sleep(3)
juego.terminarBichos()

# Terminar bichos y parar el cronómetro (simulación)
time.sleep(10)
juego.finalizar_cronometro()
juego.sumar_puntos(juego.tiempo_total())  # 1 punto por cada segundo restante

print(f"Tiempo total de partida: {juego.tiempo_total():.2f} segundos")
print(f"Puntuación final: {juego.puntuacion}")