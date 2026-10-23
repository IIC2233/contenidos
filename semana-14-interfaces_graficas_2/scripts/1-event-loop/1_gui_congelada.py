import sys
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.clicks = 0
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        self.label = QLabel("Status: esperando", self)
        self.boton_lento = QPushButton("Tarea lenta (5 segundos)", self)
        self.boton_contador = QPushButton("Clicks: 0", self)

        self.label.setGeometry(10, 10, 280, 30)
        self.boton_lento.setGeometry(10, 50, 280, 30)
        self.boton_contador.setGeometry(10, 90, 280, 30)

        self.boton_lento.clicked.connect(self.tarea_lenta)
        self.boton_contador.clicked.connect(self.contar_click)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("GUI congelada")
        self.setGeometry(50, 50, 300, 130)
        self.show()

    def tarea_lenta(self) -> None:
        """
        Este método se ejecuta en el thread principal, el mismo que corre
        el event loop. Mientras duerme, el event loop no puede procesar
        ningún otro evento: ni clicks, ni redibujar la ventana.
        """
        self.label.setText("Status: trabajando...")  # ¿Alcanza a verse?
        sleep(5)
        self.label.setText("Status: tarea lenta terminada")

    def contar_click(self) -> None:
        self.clicks += 1
        self.boton_contador.setText(f"Clicks: {self.clicks}")


if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
