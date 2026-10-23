import datetime
import json
import socket
from threading import Lock, Thread
from constantes import HOST_DEFECTO, PORT_DEFECTO
from protocolo import enviar, recibir

# Diferencia horaria de cada país respecto de UTC. Para simplificar usamos
# un valor fijo: el de Chile continental en horario de verano (UTC-3). En
# horario de invierno Chile está en UTC-4, y la hora quedaría 1 hora adelantada
DIFERENCIAS_HORARIAS = {"chile": -3, "japón": 9}


class Servidor:
    def __init__(self, host: str, port: int) -> None:
        # La lista de clientes es compartida por todos los threads que
        # atienden clientes, así que la protegemos con un Lock (semana 9)
        self.clientes = []
        self.lock_clientes = Lock()
        # Dos threads pueden enviarle al mismo cliente a la vez (la respuesta
        # a "hora" y un envío a todos). Este lock evita que los bytes de
        # ambos mensajes se mezclen en el socket y rompan el protocolo
        self.lock_envio = Lock()

        # Creamos el socket, hacemos bind y listen
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Permite reutilizar el puerto apenas se cierra el servidor. Sin esto,
        # al reiniciarlo rápido aparece "OSError: Address already in use"
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen()

    def escuchar_conexiones(self) -> None:
        print("Empezando a escuchar clientes....")
        while True:
            # Aceptamos a un cliente
            socket_cliente, direccion = self.sock.accept()
            print("Conexión aceptada desde", direccion)

            # Guardamos el socket de este cliente en la lista
            with self.lock_clientes:
                self.clientes.append(socket_cliente)

            # Creamos un thread encargado de escuchar a ese cliente
            thread = Thread(
                target=self.escuchar_cliente,
                args=(socket_cliente, direccion),
                daemon=True,
            )
            thread.start()

    # Método encargado de escuchar a 1 cliente
    def escuchar_cliente(self, socket_cliente: socket.socket, direccion: tuple) -> None:
        try:
            while True:
                mensaje = json.loads(recibir(socket_cliente).decode("utf-8"))
                print(f"[{direccion}] mandó un mensaje: {mensaje}")
                self.procesar_mensaje(mensaje, socket_cliente)

        except ConnectionError:
            print(f"[{direccion}] se desconectó")
        finally:
            # Sacamos al cliente de la lista, para no enviarle más mensajes
            with self.lock_clientes:
                self.clientes.remove(socket_cliente)
            socket_cliente.close()

    def procesar_mensaje(self, mensaje: dict, socket_cliente: socket.socket) -> None:
        if mensaje["comando"] == "cambio":
            # "adelantar" o "retrasar" afecta a TODOS los clientes conectados
            respuesta = {"tipo": "cambio", "accion": mensaje["accion"]}
            self.enviar_a_todos(respuesta)

        elif mensaje["comando"] == "hora":
            # La hora de un país se responde solo a quien la pidió
            horas = DIFERENCIAS_HORARIAS[mensaje["pais"]]
            ahora_utc = datetime.datetime.now(datetime.UTC)
            hora_pais = ahora_utc + datetime.timedelta(hours=horas)
            # Enviamos la hora como texto (ISO 8601), sin zona horaria
            respuesta = {"tipo": "hora", "hora": hora_pais.replace(tzinfo=None).isoformat()}
            self.enviar(socket_cliente, respuesta)

    def enviar(self, socket_cliente: socket.socket, mensaje: dict) -> None:
        # Cada mensaje se envía completo antes de que empiece el siguiente
        with self.lock_envio:
            enviar(socket_cliente, json.dumps(mensaje).encode("utf-8"))

    def enviar_a_todos(self, mensaje: dict) -> None:
        # Copiamos la lista dentro de lock_clientes, y enviamos fuera de él
        with self.lock_clientes:
            clientes = list(self.clientes)
        for socket_cliente in clientes:
            try:
                self.enviar(socket_cliente, mensaje)
            except OSError:
                # Ese cliente se desconectó: su propio thread lo sacará de la lista
                pass

    def cerrar(self) -> None:
        print("Cerrando socket.")
        self.sock.close()


if __name__ == "__main__":

    servidor = Servidor(HOST_DEFECTO, PORT_DEFECTO)
    try:
        servidor.escuchar_conexiones()
    except KeyboardInterrupt:
        print("Se hizo CTRL+C ... finalizando el programa.")

    servidor.cerrar()
