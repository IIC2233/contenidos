import sys
from time import sleep
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class Contador(QThread):
    senal_actualizar = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        # Bandera que el thread revisa en cada iteración de su ciclo
        self.activo = True

    def run(self) -> None:
        segundos = 0
        while self.activo:
            # Dormimos de a poco (0.1 s) para revisar la bandera seguido.
            # Si durmiéramos 10 segundos, el cierre tardaría hasta 10 segundos
            sleep(0.1)
            segundos += 0.1
            self.senal_actualizar.emit(f"Llevo {segundos:.1f} segundos")
        print("[Contador] salí del ciclo: run terminó")

    def detener(self) -> None:
        self.activo = False


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel("Status: iniciando", self)
        self.label.setGeometry(10, 10, 230, 30)
        self.setWindowTitle("Cierre limpio de un QThread")
        self.setGeometry(50, 50, 250, 50)

        self.contador = Contador()
        self.contador.senal_actualizar.connect(self.label.setText)
        self.contador.start()
        self.show()

    def closeEvent(self, evento: QCloseEvent) -> None:
        """
        closeEvent se llama cuando el usuario cierra la ventana. Antes de
        cerrar, le pedimos al thread que termine y lo esperamos con wait(),
        el equivalente a join() de threading.
        """
        print("[Ventana] cerrando: le pido al thread que se detenga")
        self.contador.detener()
        self.contador.wait()
        print("[Ventana] el thread terminó, ahora sí cierro")
        evento.accept()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
