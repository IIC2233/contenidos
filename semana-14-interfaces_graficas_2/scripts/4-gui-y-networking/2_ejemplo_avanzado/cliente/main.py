import sys
from PyQt6.QtWidgets import QApplication
from constantes import PORT_DEFECTO, HOST_DEFECTO
from frontend.ventana import MainWindow
from backend.logica import Logica

if __name__ == "__main__":

    def hook(type_, value, traceback):
        # Imprimimos el error con el hook original de Python. Al instalar
        # nuestro propio sys.excepthook, PyQt no cierra el programa
        sys.__excepthook__(type_, value, traceback)

    sys.excepthook = hook

    app = QApplication([])
    # Instanciamos nuestro backend y frontend
    backend = Logica(HOST_DEFECTO, PORT_DEFECTO)
    frontend = MainWindow()

    # Conectamos señales
    backend.senal_actualizar_etiqueta.connect(frontend.actualizar_etiqueta)
    backend.senal_desconectado.connect(frontend.mostrar_desconexion)
    frontend.senal_mandar_comando.connect(backend.mandar_comando)
    frontend.senal_pedir_hora.connect(backend.pedir_hora)
    # Justo antes de que termine la aplicación, cerramos la conexión
    app.aboutToQuit.connect(backend.cerrar)

    if not backend.conectar_a_servidor():
        sys.exit(1)

    # Mostramos la ventana y ejecutamos PyQt
    frontend.show()
    sys.exit(app.exec())
