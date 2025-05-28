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

juego.agregar_personaje("Jugador")

# Iniciar cronómetro y lanzar bichos antes del bucle
juego.iniciar_cronometro()
juego.lanzarBichos()

try:
    while True:
        # Mostrar estado antes de pedir input
        print(f"\n--- ESTADO DEL JUGADOR ---")
        print(f"Puntuación: {juego.puntuacion}")
        print(f"Vidas: {juego.personaje.vidas}")
        print(f"Llaves: {juego.personaje.llaves}")
        print(f"Habitaciones visitadas: {sorted(juego.personaje.habitaciones_visitadas)} / {len(juego.laberinto.hijos)}")
        print(f"Tiempo transcurrido: {juego.tiempo_total():.2f}s / {juego.tiempo_maximo}s")
        print(f"-------------------------")
        comando = input("Escribe el número de la habitación a la que quieres moverte (o 'salir'): \n")
        if comando.lower() == 'salir':
            print("¡Has salido del juego!")
            juego.terminarBichos()
            if juego.tiempo_fin is None:
                juego.finalizar_cronometro()
            print(f"Tiempo total de partida: {juego.tiempo_total():.2f} segundos")
            print(f"Puntuación final: {juego.puntuacion}")
            break
        num = int(comando)
        habitacion_destino = juego.obtenerHabitacion(num)
        habitacion_actual = juego.personaje.posicion

        # Buscar puerta entre habitacion_actual y habitacion_destino
        puerta_encontrada = None
        for orientacion in habitacion_actual.forma.orientaciones:
            puerta = orientacion.obtenerElemento(habitacion_actual.forma)
            if puerta and puerta.esPuerta():
                # La puerta conecta ambas habitaciones
                if (puerta.lado1 == habitacion_actual and puerta.lado2 == habitacion_destino) or \
                   (puerta.lado2 == habitacion_actual and puerta.lado1 == habitacion_destino):
                    puerta_encontrada = puerta
                    break

        if puerta_encontrada and getattr(puerta_encontrada, "bloqueada", False):
            if juego.personaje.llaves > 0:
                print("🔑 Usas una llave para abrir la puerta bloqueada.")
                juego.personaje.llaves -= 1
                puerta_encontrada.bloqueada = False
                habitacion_destino.entrar(juego.personaje)
            else:
                print("🚫 ¡La puerta está bloqueada y no tienes llaves! No puedes pasar.")
        else:
            habitacion_destino.entrar(juego.personaje)

        # Comprobar si ha ganado
        if len(juego.personaje.habitaciones_visitadas) == len(juego.laberinto.hijos):
            juego.finalizar_cronometro()
            juego.terminarBichos()
            tiempo_restante = max(0, int(juego.tiempo_maximo - juego.tiempo_total()))
            if tiempo_restante > 0:
                juego.sumar_puntos(tiempo_restante)
                print(f"¡Has ganado {tiempo_restante} puntos extra por tiempo restante!")
            print("\n🎉 ¡ENHORABUENA! Has visitado todas las habitaciones. ¡Has ganado la partida! 🎉")
            print(f"Puntuación final: {juego.puntuacion}")
            print(f"Tiempo total: {juego.tiempo_total():.2f} segundos\n")
            break

except Exception as e:
    print("Comando no válido.", e)
    juego.terminarBichos()
    if juego.tiempo_fin is None:
        juego.finalizar_cronometro()
        tiempo_restante = max(0, int(juego.tiempo_maximo - juego.tiempo_total()))
        if tiempo_restante > 0:
            juego.sumar_puntos(tiempo_restante)
    print(f"Tiempo total de partida: {juego.tiempo_total():.2f} segundos")
    print(f"Puntuación final: {juego.puntuacion}")