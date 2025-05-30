# Laberinto25 – Juego de Laberinto en Python

### Proyecto para la asignatura Diseño de Software, curso 2024-25

Este proyecto implementa la lógica y mecánicas de un videojuego de laberinto basado en patrones de diseño orientados a objetos. Es una evolución del ejemplo clásico de "Design Patterns: Elements of Reusable Object-Oriented Programming", incorporando nuevas funcionalidades que enriquecen la experiencia de juego y la arquitectura software.

---

## Descripción General

El sistema modela un laberinto compuesto por habitaciones conectadas por puertas (algunas de ellas bloqueadas con llave), cofres de recompensa, trampas, y enemigos con IA concurrente. El objetivo principal del jugador es **visitar todas las habitaciones del laberinto**, gestionando recursos como llaves y puntuación, todo ello bajo la presión de un cronómetro y la amenaza de los enemigos.

---

## Principales Patrones de Diseño Utilizados

- **Factory Method:** Creación extensible de habitaciones, puertas, paredes y otros elementos.
- **Decorator:** Añade dinamismo a elementos (por ejemplo, paredes con bombas).
- **Strategy:** Permite distintos comportamientos de enemigos (agresivo, perezoso, aleatorio).
- **Composite:** Permite recorrer y manipular la estructura jerárquica del laberinto.
- **Builder + Director:** El laberinto se genera a partir de archivos JSON externos, facilitando la configuración y extensión.
- **State:** Gestor de estados para puertas (abierta/cerrada/bloqueada) y entes (vivo/muerto).
- **Command:** Acciones como abrir puertas o activar trampas se modelan como comandos.
- **Visitor:** Recorrido polimórfico de los elementos del laberinto.
- **Singleton:** Orientaciones del mapa implementadas como instancias únicas.
- **Template Method:** Los modos de los bichos definen su algoritmo base.
  
---

## Funcionalidades y Mecánicas Extra

### 1. **Bichos con Concurrencia y un nuevo tipo**
Los enemigos se mueven y actúan de forma autónoma y paralela al jugador, pudiendo ser configurados como **agresivos**, **perezosos** o con comportamiento **aleatorio** (Bicho Loco). Cuando coinciden en una habitación con el personaje, lo atacan y pueden matarlo, terminando la partida.

### 2. **Puertas Bloqueadas con Llaves**
Algunas puertas están cerradas con llave. El jugador solo puede pasar si tiene al menos una llave, que se gasta al cruzar. Si no dispone de llaves, el paso está bloqueado. Cada llave se consume al usarla.

### 3. **Cofres de Recompensa**
En ciertas habitaciones hay cofres, que solo el personaje puede abrir (no los bichos). Los cofres otorgan puntos o llaves al abrirlos, según la configuración del JSON. Los mensajes por consola informan de su apertura y del botín conseguido.

### 4. **Trampas de Bomba**
Las bombas quitan vidas al jugador al pisarlas y se desactivan tras un solo uso.

### 5. **Puntuación Dinámica**
- Abrir puertas, recoger cofres y terminar rápido suma puntos.
- El estado de la partida, con vidas, llaves, puntuación y habitaciones visitadas, se muestra en todo momento.

### 6. **Cronómetro y Puntuación por Tiempo**
El tiempo de la partida se mide automáticamente. **El tiempo restante se convierte en puntos extra** al completar el objetivo, premiando la eficiencia.

### 7. **Control por Comandos y Mensajería Clara**
El jugador puede moverse escribiendo el número de habitación al que quiere ir. Se muestran mensajes claros tras cada acción, así como el estado actual (puntos, llaves, habitaciones visitadas, etc.).

### 8. **Interfaz por Consola Clara y Mensajería Informativa**
Todos los eventos del juego (movimiento, apertura de puertas, ataques, cofres, bombas, estado general, victoria/derrota) se informan con mensajes detallados por consola. Los cofres no se pueden volver a abrir y no se puede pasar por puertas bloqueadas sin llaves.

### 9. **Final de la Partida**
- Ganas si visitas todas las habitaciones antes de que acabe el tiempo.
- Pierdes si te quedas sin vidas (por ataques o trampas) o si expira el cronómetro.
- El juego muestra el estado actual (vidas, puntuación, llaves, habitaciones visitadas, tiempo transcurrido) tras cada acción.

---

## Estructura del Proyecto

- `juego.py`: Lógica principal del juego, control de flujo, puntuación y tiempo.
- `director.py`, `laberinto_builder.py`: Interpretación del archivo JSON y construcción dinámica del laberinto.
- `habitacion.py`, `puerta.py`, `pared.py`, `bomba.py`: Elementos del mapa.
- `bicho.py`, `bicholoco.py`, `agresivo.py`, `perezoso.py`, `modo.py`: IA y comportamientos de los enemigos.
- `cofre.py`: Lógica de cofres de puntos y llaves.
- `ente.py`: Base para personaje y enemigos.
- `builder_example.py`: Script principal de ejecución y control por comandos.
- `README.md`: Documentación y explicación del proyecto.

---

## Ejemplo de Archivo JSON de Configuración

```json
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

```

---

## Cómo Jugar
- Modifica o crea tu archivo JSON de configuración en /laberintos/.
- Ejecuta el juego con el script principal (builder_example.py).
- El juego te pedirá por consola a qué habitación quieres moverte. Introduce el número y pulsa Enter.
- Lee el estado del jugador tras cada acción y sigue hasta visitar todas las habitaciones o agotar el tiempo/vidas.

## Diagrama de Clases

![Diagrama_clases](https://github.com/user-attachments/assets/1cbe8464-671c-43d3-a436-054d392708e4)

## Desarrollado por Francisco del Sol Ontalba para la asignatura Diseño de Software (curso 2024-25) en la Universidad de Castilla-La Mancha.
