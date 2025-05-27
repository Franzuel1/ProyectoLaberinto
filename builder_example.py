from director import Director
import time

director = Director()

# Cambia esta línea para apuntar al archivo que incluye al BichoLoco
filename = "./laberintos/laberinto_bicholoco.json"

data = director.leerArchivo(filename)
if data:
    print("Datos cargados del JSON:")
    print(data)
else:
    print("Error al cargar JSON.")

director.procesar(filename)
juego = director.obtenerJuego()

# Ejemplo de recorrido del laberinto
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

# Mostrar los bichos del juego (debe aparecer aquí el BichoLoco)
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")

# Abrir puertas y lanzar los bichos
juego.abrir_puertas()
juego.lanzarBichos()
time.sleep(3)
juego.terminarBichos()

# Terminar bichos y parar el cronómetro (simulación)
import time
time.sleep(20)  # Dejar que el juego corra 20 segundos
juego.finalizar_cronometro()

print(f"Tiempo total de partida: {juego.tiempo_total():.2f} segundos")
