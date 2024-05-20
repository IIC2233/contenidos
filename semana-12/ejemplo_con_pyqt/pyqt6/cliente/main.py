from backend import backend
from frontend import ventana
from PyQt6.QtWidgets import QApplication
from constantes import PORT_DEFECTO, HOST_DEFECTO
import sys

if __name__ == "__main__":
    # Hook para imprimir errores
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication(sys.argv)

    # Usamos nuestras constantes
    host = HOST_DEFECTO
    port = PORT_DEFECTO

    # Instanciamos nuestro backend y frontend
    back = backend.Logica(host, port)
    frontend = ventana.MainWindow()

    # Conectamos señales
    back.senal_update_label.connect(frontend.update_label)
    frontend.senal_mandar_comando.connect(back.mandar_comando)

    # Mostramos la ventana y ejecutamos pyqt
    frontend.show()
    sys.exit(app.exec())
