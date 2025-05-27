from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        alguien.posicion = self
        # Buscar cofres y abrirlos
        if hasattr(self, "hijos"):
            for hijo in self.hijos:
                # Si es un cofre, lo abrimos
                from cofre import Cofre
                if isinstance(hijo, Cofre):
                    hijo.abrir(alguien, alguien.juego)

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
    def calcularPosicion(self):
        self.forma.calcularPosicion()
    def __str__(self):
        return "Soy una habitacion"
