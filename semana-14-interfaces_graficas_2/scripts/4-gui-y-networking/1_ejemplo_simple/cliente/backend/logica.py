import socket
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from protocolo import enviar, recibir


# Primero definimos un QThread que recibe el socket y se dedica
# exclusivamente a escuchar al servidor. recv es bloqueante, por eso
# no puede ejecutarse en el thread principal: congelaría la interfaz
class EscucharQThread(QThread):
    # Señal que entrega cada mensaje recibido al componente lógico
    senal_mensaje = pyqtSignal(str)
    # Señal que avisa que se perdió la conexión
    senal_desconectado = pyqtSignal()

    def __init__(self, socket_cliente: socket.socket) -> None:
        super().__init__()
        self.socket_cliente = socket_cliente

    def run(self) -> None:
        print("Levantando el thread que escucha al servidor...")
        try:
            while True:
                mensaje = recibir(self.socket_cliente).decode("utf-8")
                # Emitimos la señal con el mensaje decodificado
                self.senal_mensaje.emit(mensaje)
        except (ConnectionError, OSError):
            # El servidor se cayó, o nosotros cerramos el socket
            print("Dejé de escuchar al servidor")
            self.senal_desconectado.emit()


# En este componente lógico instanciamos el socket, y definimos el envío
# y procesamiento de mensajes. Para escuchar usa el QThread anterior
class Logica(QObject):

    senal_actualizar_etiqueta = pyqtSignal(str)
    senal_desconectado = pyqtSignal()

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_escuchar = None

    def conectar_a_servidor(self) -> bool:
        try:
            self.socket_cliente.connect((self.host, self.port))
        except ConnectionError:
            print("No me pude conectar al servidor.")
            return False

        print("Cliente conectado exitosamente al servidor.")
        # Creamos el thread que escucha y guardamos su referencia
        self.thread_escuchar = EscucharQThread(self.socket_cliente)
        self.thread_escuchar.senal_mensaje.connect(self.procesar_mensaje)
        self.thread_escuchar.senal_desconectado.connect(self.senal_desconectado)
        self.thread_escuchar.start()
        return True

    # Aquí procesamos el contenido del mensaje.
    # Para este ejemplo, solo lo mandamos al frontend
    def procesar_mensaje(self, mensaje: str) -> None:
        self.senal_actualizar_etiqueta.emit(mensaje)

    def mandar_comando(self, comando: str) -> None:
        try:
            enviar(self.socket_cliente, comando.encode("utf-8"))
        except (ConnectionError, OSError):
            self.senal_desconectado.emit()

    def cerrar(self) -> None:
        # shutdown despierta al recv que está bloqueado en el otro thread
        # (le hace retornar b""), así el thread termina por sí solo
        try:
            self.socket_cliente.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass  # El socket ya estaba desconectado
        self.socket_cliente.close()
        if self.thread_escuchar is not None:
            self.thread_escuchar.wait()
