import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class Cronometro(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Décimas de segundo transcurridas
        self.decimas = 0

        # Este QTimer avanza el cronómetro cada 100 ms. No lo iniciamos aún
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.avanzar)

        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        self.label = QLabel(self)
        self.label.setFont(QFont("Monospace", 30))
        self.label.setGeometry(10, 10, 230, 50)

        self.boton_pausa = QPushButton("Iniciar", self)
        self.boton_pausa.setGeometry(10, 70, 110, 30)
        self.boton_pausa.clicked.connect(self.pausar_o_reanudar)

        self.boton_reiniciar = QPushButton("Reiniciar", self)
        self.boton_reiniciar.setGeometry(130, 70, 110, 30)
        self.boton_reiniciar.clicked.connect(self.reiniciar)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Cronómetro con QTimer")
        self.setGeometry(50, 50, 250, 110)
        self.actualizar_label()
        self.show()

    def avanzar(self) -> None:
        self.decimas += 1
        self.actualizar_label()

    def pausar_o_reanudar(self) -> None:
        # isActive() nos dice si el QTimer está corriendo.
        # Pausar es simplemente detener el QTimer, y reanudar es
        # volver a iniciarlo. El estado (self.decimas) no se pierde
        if self.timer.isActive():
            self.timer.stop()
            self.boton_pausa.setText("Reanudar")
        else:
            self.timer.start()
            self.boton_pausa.setText("Pausar")

    def reiniciar(self) -> None:
        self.timer.stop()
        self.decimas = 0
        self.boton_pausa.setText("Iniciar")
        self.actualizar_label()

    def actualizar_label(self) -> None:
        minutos, decimas = divmod(self.decimas, 600)
        self.label.setText(f"{minutos:02d}:{decimas / 10:04.1f}")


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    cronometro = Cronometro()
    sys.exit(app.exec())
