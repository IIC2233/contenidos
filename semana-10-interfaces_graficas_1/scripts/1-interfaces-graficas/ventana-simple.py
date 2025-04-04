import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional).
        self.setWindowTitle('Mi Primera Ventana')


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])  # Creamos las base de la app: QApplication.
    ventana = MiVentana()   # Construimos un QWidget que será nuestra ventana.
    ventana.show()          # Mostramos la ventana.
    sys.exit(app.exec())    # La aplicación se inicia con app.exec().
                            # Esto habilita el loop de eventos y retorna un
                            # código de salida que luego lo toma "sys.exit()".
