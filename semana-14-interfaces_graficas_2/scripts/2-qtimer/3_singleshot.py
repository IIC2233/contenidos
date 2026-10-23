from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
import sys
import datetime


class RelojDigital(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Crear label encargado de mostrar la hora
        self.label_timer = QLabel()
        self.label_timer.setFont(QFont("Times", 50))

        # Crear layout vertical para nuestro label
        layout = QVBoxLayout()
        layout.addWidget(self.label_timer)
        self.setLayout(layout)

        # Crear nuestro QTimer encargado de actualizar el tiempo cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrar_hora)
        self.timer.setInterval(1000)
        self.timer.start()

        # Definir título y tamaño ventana
        self.setWindowTitle("Reloj Digital con QTimer")
        self.setGeometry(100, 100, 250, 100)

        # Ejecutar el método para mostrar hora por primera vez
        self.mostrar_hora()

        # Mostrar ventana
        self.show()

        # Forma 1: un QTimer configurado con setSingleShot(True).
        # Después de 3 segundos esconde la ventana, y no se vuelve a ejecutar
        self.timer_esconder = QTimer(self)
        self.timer_esconder.setSingleShot(True)
        self.timer_esconder.timeout.connect(self.hide)
        self.timer_esconder.setInterval(3000)
        self.timer_esconder.start()

        # Forma 2: el método estático QTimer.singleShot, sin crear un objeto.
        # Después de 5 segundos vuelve a mostrar la ventana
        QTimer.singleShot(5000, self.show)

    def mostrar_hora(self) -> None:
        # Obtener hora actual
        hora_actual = datetime.datetime.now().time()
        # Actualizar texto del label
        self.label_timer.setText(hora_actual.strftime("%H:%M:%S"))


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    reloj = RelojDigital()
    sys.exit(app.exec())
