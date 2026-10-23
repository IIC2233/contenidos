import sys
import threading
from time import sleep
from PyQt6.QtCore import pyqtSignal, QObject, QThread
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def donde_estoy() -> str:
    if threading.current_thread() is threading.main_thread():
        return "thread PRINCIPAL"
    return "thread SECUNDARIO"


class Trabajador(QObject):
    """
    Un QObject común y corriente (NO hereda de QThread). Sus métodos se
    ejecutarán en el thread al que lo movamos con moveToThread.
    """

    senal_progreso = pyqtSignal(str)
    senal_terminado = pyqtSignal()

    def trabajar(self) -> None:
        print(f"[trabajar] me ejecuto en el {donde_estoy()}")
        for i in range(1, 6):
            sleep(0.5)
            self.senal_progreso.emit(f"Paso {i} de 5")
        self.senal_progreso.emit("Status: trabajo terminado")
        self.senal_terminado.emit()


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel("Status: esperando", self)
        self.boton = QPushButton("Trabajar", self)
        self.label.setGeometry(10, 10, 230, 30)
        self.boton.setGeometry(10, 50, 230, 30)
        self.boton.clicked.connect(self.iniciar)
        self.setWindowTitle("Patrón worker + moveToThread")
        self.setGeometry(50, 50, 250, 90)

        # 1. Creamos un QThread "vacío": su run por defecto solo corre un
        #    event loop para ese thread
        self.mi_thread = QThread()
        # 2. Creamos el trabajador y lo movemos a ese thread
        self.trabajador = Trabajador()
        self.trabajador.moveToThread(self.mi_thread)
        # 3. Conectamos señales
        self.trabajador.senal_progreso.connect(self.label.setText)
        self.trabajador.senal_terminado.connect(self.mi_thread.quit)
        self.mi_thread.started.connect(self.trabajador.trabajar)
        self.show()

    def iniciar(self) -> None:
        if not self.mi_thread.isRunning():
            self.mi_thread.start()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
