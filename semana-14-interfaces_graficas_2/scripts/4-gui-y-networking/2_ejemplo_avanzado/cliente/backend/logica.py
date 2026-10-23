import datetime
import json
import socket
from PyQt6.QtCore import QObject, QThread, QTimer, pyqtSignal
from protocolo import enviar, recibir


# Mismo QThread del ejemplo simple, pero ahora los mensajes son diccionarios
# serializados con JSON
class EscucharQThread(QThread):
    senal_mensaje = pyqtSignal(dict)
    senal_desconectado = pyqtSignal()

    def __init__(self, socket_cliente: socket.socket) -> None:
        super().__init__()
        self.socket_cliente = socket_cliente

    def run(self) -> None:
        print("Levantando el thread que escucha al servidor...")
        try:
            while True:
                mensaje = json.loads(recibir(self.socket_cliente).decode("utf-8"))
                self.senal_mensaje.emit(mensaje)
        except (ConnectionError, OSError):
            print("Dejé de escuchar al servidor")
            self.senal_desconectado.emit()


class Logica(QObject):

    senal_actualizar_etiqueta = pyqtSignal(str)
    senal_desconectado = pyqtSignal()

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_escuchar = None

        # El reloj avanza 1 segundo cada 1 segundo: una tarea periódica y
        # corta, así que usamos un QTimer. Todo ocurre en el thread
        # principal, por lo que self.hora_actual no necesita un lock
        self.hora_actual = None
        self.timer_reloj = QTimer(self)
        self.timer_reloj.setInterval(1000)
        self.timer_reloj.timeout.connect(self.avanzar_reloj)

    def conectar_a_servidor(self) -> bool:
        try:
            self.socket_cliente.connect((self.host, self.port))
        except ConnectionError:
            print("No me pude conectar al servidor.")
            return False

        print("Cliente conectado exitosamente al servidor.")
        # Recibir mensajes es bloqueante, así que usamos un QThread
        self.thread_escuchar = EscucharQThread(self.socket_cliente)
        self.thread_escuchar.senal_mensaje.connect(self.procesar_mensaje)
        self.thread_escuchar.senal_desconectado.connect(self.desconectado)
        self.thread_escuchar.start()
        self.pedir_hora("chile")
        return True

    # Aquí procesamos el contenido del mensaje
    def procesar_mensaje(self, mensaje: dict) -> None:
        if mensaje["tipo"] == "hora":
            self.hora_actual = datetime.datetime.fromisoformat(mensaje["hora"])
            if not self.timer_reloj.isActive():
                self.timer_reloj.start()

        elif mensaje["tipo"] == "cambio" and self.hora_actual is not None:
            una_hora = datetime.timedelta(hours=1)
            if mensaje["accion"] == "adelantar":
                self.hora_actual += una_hora
            else:  # mensaje["accion"] == "retrasar"
                self.hora_actual -= una_hora

        self.actualizar_etiqueta()

    def avanzar_reloj(self) -> None:
        self.hora_actual += datetime.timedelta(seconds=1)
        self.actualizar_etiqueta()

    def actualizar_etiqueta(self) -> None:
        if self.hora_actual is not None:
            self.senal_actualizar_etiqueta.emit(self.hora_actual.strftime("%Y-%m-%d %H:%M:%S"))

    def desconectado(self) -> None:
        self.timer_reloj.stop()
        self.senal_desconectado.emit()

    def enviar(self, mensaje: dict) -> None:
        try:
            enviar(self.socket_cliente, json.dumps(mensaje).encode("utf-8"))
        except (ConnectionError, OSError):
            self.desconectado()

    def mandar_comando(self, comando: str) -> None:
        # comando es "adelantar" o "retrasar"
        self.enviar({"comando": "cambio", "accion": comando})

    def pedir_hora(self, pais: str) -> None:
        self.enviar({"comando": "hora", "pais": pais})

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
