import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)
from PyQt5.QtGui import QKeyEvent


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.estado = QLabel('No se está presionando una tecla.', self)
        self.estado.move(20, 10)
        self.resize(self.estado.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Teclado')
        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Este método maneja el evento que se produce al presionar las teclas.
        """
        self.estado.setText(f'Presionaron la tecla: {event.text()} '
                            f'de código: {event.key()}')
        self.estado.resize(self.estado.sizeHint())

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        """
        Este método maneja el evento que se produce al liberar una tecla.
        """
        self.estado.setText('No se está presionando una tecla.')
        self.estado.resize(self.estado.sizeHint())


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
