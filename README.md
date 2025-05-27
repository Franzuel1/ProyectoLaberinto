## Laberinto25 – Diseño y Expansión del Laberinto en Python
# Proyecto de la asignatura Diseño de Software, curso 2024-25
Este proyecto desarrolla la lógica y estructura de un videojuego de laberinto basado en patrones de diseño, con una arquitectura extensible y varias mecánicas adicionales. La inspiración parte de los ejemplos del libro "Design Patterns: Elements of Reusable Object-Oriented Programming", ampliando el juego clásico con nuevas funcionalidades orientadas a la jugabilidad y la demostración de principios SOLID.

## Descripción General
El sistema implementa un laberinto compuesto por habitaciones conectadas mediante puertas, algunas de ellas bloqueadas, con trampas (bombas), enemigos con distintos comportamientos y un sistema de recompensas. El jugador debe recorrer el laberinto, evitar o enfrentarse a los enemigos y recoger tesoros o llaves, todo ello gestionado mediante un cronómetro y una puntuación dinámica.

## Patrones de Diseño Utilizados
El código hace uso de múltiples patrones de diseño clásicos, adaptados para modelar tanto la estructura del juego como el comportamiento de los entes y objetos del laberinto:

# Factory Method
Permite la creación flexible y escalable de habitaciones, paredes, puertas y otros elementos del mapa, facilitando la extensión mediante subclases específicas para habitaciones con bombas, bichos especiales, etc.

# Decorator
Utilizado para añadir dinamismo a elementos como las paredes, a las que se les pueden incorporar bombas y otras responsabilidades adicionales sin modificar la clase base.

# Strategy
Cada enemigo ("bicho") puede comportarse de manera diferente gracias a la encapsulación de algoritmos de movimiento y ataque (por ejemplo, modos agresivo o perezoso), intercambiables en tiempo de ejecución.

# Composite
Estructura el laberinto y sus habitaciones permitiendo tratar uniformemente elementos individuales y colecciones (habitaciones, puertas, cofres, etc.), facilitando el recorrido y manipulación recursiva de la estructura del mapa.

# Builder
El laberinto se genera a partir de archivos JSON, que describen la forma, las habitaciones, las conexiones y los elementos extra (cofres, bichos, bombas, etc.). Un director interpreta este archivo y coordina el proceso de creación de todos los componentes del juego.

# State
Aplicado a las puertas (abierta/cerrada/bloqueada) y a los entes (vivo/muerto), encapsulando el comportamiento dependiente del estado de cada objeto.

# Command
Todas las acciones importantes (abrir/cerrar puertas, activar bombas, entrar en habitaciones) están modeladas como comandos, lo que permite su gestión flexible, almacenamiento y posible deshacer.

# Visitor
El patrón Visitor se utiliza para recorrer los distintos elementos del laberinto y permitir operaciones genéricas sobre los distintos tipos de objetos sin modificar sus clases.

# Singleton
Las orientaciones (Norte, Sur, Este, Oeste) están modeladas como instancias únicas, evitando duplicidad y facilitando la comparación e interoperabilidad.

# Template Method
El método actua de los modos de los bichos utiliza este patrón, permitiendo definir el esqueleto de un algoritmo y delegar en subclases los pasos específicos (dormir, caminar, atacar, etc.).

## Nuevas Funcionalidades y Extras Implementados
Durante el desarrollo se han añadido varias mecánicas extra que enriquecen la experiencia de juego:

# 1. Nuevos Tipos de Bichos
Se ha incorporado un "Bicho Loco", un enemigo con comportamiento aleatorio que añade imprevisibilidad al recorrido del laberinto. Los bichos pueden estar en modo agresivo, perezoso, o loco, y son configurables desde el archivo JSON.

# 2. Sistema de Cronómetro
El juego mide el tiempo de la partida de forma precisa. El cronómetro comienza al iniciar el juego y puede consultarse o detenerse en cualquier momento, añadiendo un reto temporal o permitiendo crear rankings según la velocidad de resolución.

# 3. Puntuación Dinámica
Cada acción relevante en el juego suma o resta puntos: abrir puertas, superar enemigos o recoger recompensas. El sistema de puntos se actualiza en tiempo real, permitiendo evaluar la eficiencia del jugador al final de la partida.

# 4. Puertas Bloqueadas y Llaves
Algunas puertas del laberinto pueden estar bloqueadas y solo se abren utilizando una llave, la cual debe encontrarse durante el recorrido. El sistema de llaves es completamente funcional, controlando el acceso a zonas restringidas y añadiendo estrategia al uso de los recursos.

# 5. Cofres y Recompensas Aleatorias
En determinadas habitaciones pueden encontrarse cofres que otorgan recompensas al jugador. Al abrir un cofre (automáticamente al entrar el personaje), se recibe una cantidad de puntos o llaves, elegida de forma configurable o aleatoria. Los cofres no pueden ser abiertos por enemigos, sólo por el personaje principal.

## Estructura del Proyecto
juego.py: Lógica principal del juego y orquestación de los elementos.

director.py y laberinto_builder.py: Patrones Builder/Director para interpretar el JSON y construir la estructura del laberinto.

habitacion.py, puerta.py, pared.py: Modelado de las habitaciones y conexiones.

bicho.py, bicholoco.py: Enemigos y sus comportamientos.

cofre.py: Implementación de los cofres de recompensa.

ente.py: Clase base para personaje y bichos.

README.md: Documentación y explicación detallada del proyecto.

## Ejemplo de Archivo JSON de Configuración
El siguiente es un ejemplo de cómo se puede definir un laberinto personalizado con enemigos, bombas, puertas bloqueadas y cofres de recompensa:

json
Copiar código
{
  "forma": "cuadrado",
  "laberinto": [
    {"tipo": "habitacion", "num": 1, "hijos": [{"tipo": "bomba"}]},
    {"tipo": "habitacion", "num": 2, "hijos": [
      {"tipo": "cofre", "tipo_recompensa": "puntos", "cantidad": 12}
    ]},
    {"tipo": "habitacion", "num": 3, "hijos": [
      {"tipo": "cofre", "tipo_recompensa": "llaves", "cantidad": 2}
    ]},
    {"tipo": "habitacion", "num": 4, "hijos": [{"tipo": "bomba"}]}
  ],
  "puertas": [
    [1, "Sur", 2, "Norte", {"bloqueada": true}],
    [2, "Oeste", 3, "Este"],
    [3, "Sur", 4, "Norte"]
  ],
  "bichos": [
    {"modo": "Agresivo", "posicion": 1},
    {"modo": "Perezoso", "posicion": 4},
    {"tipo": "bicholoco", "posicion": 2}
  ]
}

## Cómo Ejecutar el Juego
Modifica o crea tu archivo JSON de configuración en la carpeta /laberintos/.

Lanza el juego usando el script principal (builder_example.py o equivalente).

El juego mostrará por consola la evolución del personaje, los encuentros con enemigos y la recogida de recompensas.

## Imágenes y Diagramas
AÑADIR DIAGRAMAS

## Autoría y Créditos
Desarrollado por Francisco del Sol Ontalba para la asignatura Diseño de Software (curso 24-25) en la Universidad de Castilla-La Mancha.