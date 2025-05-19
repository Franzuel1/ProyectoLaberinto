# ProyectoLaberinto

Este proyecto es una implementación de un juego de laberinto en Python basado en patrones de diseño como Factory Method, Decorator, Strategy y Composite. El objetivo es moverse a través del laberinto, enfrentarse a bichos, esquivar bombas y alcanzar la salida.

## Archivos principales

juego.py: Contiene la lógica principal del juego, incluyendo las clases Juego, Habitacion, Bomba, Bicho, y sus comportamientos.

creator.py: Implementa el patrón Factory Method para crear diferentes estructuras de laberinto.

main.py: Punto de entrada principal del juego. Aquí se inicia y ejecuta la lógica del laberinto.

.gitignore: Define los archivos y carpetas a ignorar en el control de versiones.

README.md: Documentación del proyecto.

## Patrones de Diseño Utilizados

Factory Method: Permite crear diferentes tipos de laberintos a través de las clases CreatorBasico y CreatorAvanzado.

Decorator: Añade funcionalidades como bombas a las habitaciones.

Strategy: Define los comportamientos de los bichos (BichoPerezoso, BichoAgresivo).

Composite: Modela la estructura del laberinto, permitiendo tratar habitaciones y elementos de manera uniforme.

![image](https://github.com/user-attachments/assets/c9814ee6-2680-4bb3-95ed-da839d0f6510)
![image](https://github.com/user-attachments/assets/519146c8-30f2-4b0c-a0ee-de7ab49d65df)

## Ejemplo de Uso

Al ejecutar el juego, el sistema te guiará a través del laberinto. Puedes moverte utilizando las teclas:

N → Norte

S → Sur

E → Este

O → Oeste

Interactuarás con diferentes elementos como bombas y bichos mientras exploras el laberinto.
