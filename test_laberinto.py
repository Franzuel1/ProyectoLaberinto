import unittest
from juego import Juego
from habitacion import Habitacion
from cofre import Cofre
from bomba import Bomba
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from ente import Personaje

class TestLaberinto(unittest.TestCase):

    def setUp(self):
        self.juego = Juego()
        self.h1 = Habitacion(1)
        self.h2 = Habitacion(2)
        self.h1.hijos = []
        self.h2.hijos = []
        self.juego.laberinto = type("FakeLab", (), {})()
        self.juego.laberinto.hijos = [self.h1, self.h2]
        self.juego.personaje = Personaje(vidas=10, poder=1, juego=self.juego, nombre="TestPlayer")
        self.juego.personaje.posicion = self.h1

    def test_cofre_puntos(self):
        cofre = Cofre(tipo_recompensa="puntos", cantidad=10)
        self.h1.hijos.append(cofre)
        puntos_antes = self.juego.puntuacion
        cofre.abrir(self.juego.personaje, self.juego)
        # Verifica que el cofre suma puntos y se marca como abierto
        self.assertGreater(self.juego.puntuacion, puntos_antes)
        self.assertTrue(cofre.abierto)
        # Probar que abrirlo otra vez NO suma puntos de nuevo
        puntos_despues = self.juego.puntuacion
        cofre.abrir(self.juego.personaje, self.juego)
        self.assertEqual(self.juego.puntuacion, puntos_despues)

    def test_cofre_llaves(self):
        cofre = Cofre(tipo_recompensa="llaves", cantidad=2)
        self.h1.hijos.append(cofre)
        llaves_antes = self.juego.personaje.llaves
        cofre.abrir(self.juego.personaje, self.juego)
        # Debe sumar llaves y marcarse abierto
        self.assertGreater(self.juego.personaje.llaves, llaves_antes)
        self.assertTrue(cofre.abierto)
        # Probar que abrirlo otra vez NO suma llaves de nuevo
        llaves_despues = self.juego.personaje.llaves
        cofre.abrir(self.juego.personaje, self.juego)
        self.assertEqual(self.juego.personaje.llaves, llaves_despues)

    def test_bomba(self):
        bomba = Bomba(None)
        self.h1.hijos.append(bomba)
        vidas_antes = self.juego.personaje.vidas
        # Entrar en la habitación activa la bomba la primera vez
        self.h1.entrar(self.juego.personaje)
        self.assertLess(self.juego.personaje.vidas, vidas_antes)
        vidas_despues = self.juego.personaje.vidas
        # Entrar otra vez NO debe hacer daño (bomba desactivada)
        self.h1.entrar(self.juego.personaje)
        self.assertEqual(self.juego.personaje.vidas, vidas_despues)

    def test_bicho_agresivo_ataca(self):
        bicho = Bicho()
        bicho.iniAgresivo()
        bicho.posicion = self.h1
        self.juego.personaje.posicion = self.h1
        bicho.juego = self.juego
        vidas_antes = self.juego.personaje.vidas
        bicho.modo.atacar(bicho)
        self.assertLess(self.juego.personaje.vidas, vidas_antes)
        # Si el ataque es letal, el personaje debe quedarse sin vidas
        self.juego.personaje.vidas = bicho.poder
        bicho.modo.atacar(bicho)
        self.assertLessEqual(self.juego.personaje.vidas, 0)

    def test_bicho_perezoso_ataca(self):
        bicho = Bicho()
        bicho.iniPerezoso()
        bicho.posicion = self.h1
        self.juego.personaje.posicion = self.h1
        bicho.juego = self.juego
        vidas_antes = self.juego.personaje.vidas
        Perezoso().atacar(bicho)
        self.assertLess(self.juego.personaje.vidas, vidas_antes)
        # Probar ataque cuando personaje NO está en la misma habitación (no hace daño)
        bicho.posicion = self.h2
        vidas_antes = self.juego.personaje.vidas
        Perezoso().atacar(bicho)
        self.assertEqual(self.juego.personaje.vidas, vidas_antes)

    def test_puerta_bloqueada_sin_llave(self):
        from puerta import Puerta
        self.juego.personaje.llaves = 0
        puerta = Puerta(self.h1, self.h2, bloqueada=True)
        # Intentar abrir sin llave no debe desbloquear la puerta
        puerta.abrir(tiene_llave=False)
        self.assertTrue(puerta.bloqueada)
        # Darle una llave y abrir, ahora sí debe desbloquearse
        self.juego.personaje.llaves = 1
        puerta.abrir(tiene_llave=True)
        self.assertFalse(puerta.bloqueada)

if __name__ == '__main__':
    unittest.main()
