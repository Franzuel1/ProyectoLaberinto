from decorator import Decorator

class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = True  # La bomba empieza activa

    def esBomba(self):
        return True

    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)

    def __str__(self):
        return "Soy una bomba"

    def entrar(self, alguien):
        from ente import Personaje
        if isinstance(alguien, Personaje) and self.activa:
            alguien.recibir_daño(2)
            print(f"💥 ¡Has pisado una bomba! Pierdes 2 vidas. Vidas restantes: {alguien.vidas}")
            self.activa = False  # Se desactiva después de explotar
        super().entrar(alguien)