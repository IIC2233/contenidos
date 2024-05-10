import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QFont, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit

import reloj

# Puedes importar otras librerías si gustas


class VentanaReloj(QWidget):
    pausar_signal = pyqtSignal()
    reiniciar_signal = pyqtSignal()
    cambiar_hora_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.reloj = None

    def init_GUI(self):
        self.hora = QLabel("00:00:00", self)  # corresponde a la hora del reloj
        self.tiempo = QLabel(
            "00:00:00:00", self
        )  # corresponde al tiempo del cronómetro

        self.linea_hora = QLineEdit("Ej: 00:00:00", self)
        self.linea_hora.setGeometry(45, 15, 100, 20)
        # Completar y modificar
        self.hora.hide()
        self.tiempo.hide()
        self.linea_hora.hide()

    def avance_del_tiempo(self, hora, minutos, segundos):
        self.hora.setText(f"{hora:02}:{minutos:02}:{segundos:02}")

    def cronometro_corriendo(self, hora, minutos, segundos, milesimas):
        self.tiempo.setText(f"{hora:02}:{minutos:02}:{segundos:02}:{milesimas:02}")

    def iniciar_cronometro(self):
        self.reloj.comenzar_cronometro()
        # Completar
        pass

    def reiniciar_cronometro(self):
        self.pausar_signal.emit()
        self.reiniciar_signal.emit()
        # Completar
        pass

    def pausar_cronometro(self):
        self.pausar_signal.emit()
        # Completar
        pass

    def cambiar_hora(self):
        self.cambiar_hora_signal.emit(self.linea_hora.text())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Completar

        # A continuación viene la instanciación de la ventana y del reloj y las conexiones de las señales.
        self.front_end_reloj = VentanaReloj()
        self.front_end_reloj.reloj = reloj.Reloj()

        self.front_end_reloj.reiniciar_signal.connect(
            self.front_end_reloj.reloj.reiniciar_cronometro
        )
        self.front_end_reloj.pausar_signal.connect(
            self.front_end_reloj.reloj.pausar_cronometro
        )
        self.front_end_reloj.cambiar_hora_signal.connect(
            self.front_end_reloj.reloj.cambiar_hora
        )

        self.front_end_reloj.reloj.actualizar_hora_signal.connect(
            self.front_end_reloj.avance_del_tiempo
        )
        self.front_end_reloj.reloj.actualizar_cronometro_signal.connect(
            self.front_end_reloj.cronometro_corriendo
        )

        self.front_end_reloj.reloj.comenzar_reloj()
        self.setCentralWidget(self.front_end_reloj)

    def pagina_cronometro(self):
        # Completar
        pass

    def pagina_hora(self):
        # Completar
        pass

    def cambiar_hora(self):
        # Completar
        pass


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
