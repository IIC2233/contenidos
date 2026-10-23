from PyQt6.QtWidgets import QApplication
from frontend.ventana import Ventana
import sys
import parametros_general as p
from backend.logica_qthread import Juego

# El mismo juego está implementado con 3 back-ends distintos. Para probar
# otro, cambia la línea 5 por una de las siguientes:
# from backend.logica_thread import Juego   # threading.Thread
# from backend.logica_qtimer import Juego   # QTimer


class Simulacion:
    def __init__(self) -> None:
        # Instanciamos nuestros objeto Ventana y Juego
        self.frontend = Ventana(p.TAMAÑO_VENTANA)
        self.backend = Juego(p.TAMAÑO_VENTANA)

    # Conectamos señales
    def conectar(self) -> None:
        # Frontend notifica al backend cuando queremos detener un cuadrado
        self.frontend.senal_parar_icono.connect(self.backend.parar_icono)

        # Backend notifica al frontend cuando empieza todo, aparece un ícono
        # y se mueve un ícono
        self.backend.senal_empezar.connect(self.frontend.empezar)
        self.backend.senal_aparecer_icono.connect(self.frontend.aparecer_icono)
        self.backend.senal_mover_icono.connect(self.frontend.mover_icono)

    # Empezamos todo. En este caso es el backend quien comienza la ejecución de todo
    def iniciar(self) -> None:
        self.backend.empezar()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook

    app = QApplication([])
    simulacion = Simulacion()
    simulacion.conectar()
    simulacion.iniciar()
    # Antes de terminar, le pedimos al back-end que detenga todo
    app.aboutToQuit.connect(simulacion.backend.detener)

    sys.exit(app.exec())
