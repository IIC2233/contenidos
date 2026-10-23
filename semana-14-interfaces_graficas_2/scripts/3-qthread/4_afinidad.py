import sys
import threading
from time import sleep
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def donde_estoy() -> str:
    # Usamos threading (semana 9) para saber en qué thread se ejecuta el código
    if threading.current_thread() is threading.main_thread():
        return "thread PRINCIPAL"
    return "thread SECUNDARIO"


class MiThread(QThread):
    senal_progreso = pyqtSignal(str)

    def run(self) -> None:
        # run es lo único que se ejecuta en el thread nuevo
        print(f"[run] me ejecuto en el {donde_estoy()}")
        for i in range(1, 6):
            sleep(1)
            self.senal_progreso.emit(f"Paso {i} de 5")
        self.senal_progreso.emit("Status: QThread terminado")

    def tarea_pesada(self) -> None:
        # Este método es un slot del QThread. ¿Dónde se ejecuta?
        print(f"[tarea_pesada] me ejecuto en el {donde_estoy()}")
        sleep(3)
        print("[tarea_pesada] terminé")


class MiVentana(QWidget):
    senal_pedir_tarea = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        print(f"[__init__ de MiVentana] me ejecuto en el {donde_estoy()}")
        self.mi_thread = MiThread()
        self.mi_thread.senal_progreso.connect(self.actualizar_label)
        self.senal_pedir_tarea.connect(self.mi_thread.tarea_pesada)
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        self.label = QLabel("Status: esperando QThread", self)
        self.boton_iniciar = QPushButton("Iniciar QThread", self)
        self.boton_tarea = QPushButton("Pedirle una tarea pesada al QThread", self)

        self.label.setGeometry(10, 10, 330, 30)
        self.boton_iniciar.setGeometry(10, 50, 330, 30)
        self.boton_tarea.setGeometry(10, 90, 330, 30)

        self.boton_iniciar.clicked.connect(self.iniciar_thread)
        self.boton_tarea.clicked.connect(self.senal_pedir_tarea.emit)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Afinidad de threads")
        self.setGeometry(50, 50, 350, 130)
        self.show()

    def iniciar_thread(self) -> None:
        if not self.mi_thread.isRunning():
            self.mi_thread.start()

    def actualizar_label(self, texto: str) -> None:
        print(f"[actualizar_label] me ejecuto en el {donde_estoy()}")
        self.label.setText(texto)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
