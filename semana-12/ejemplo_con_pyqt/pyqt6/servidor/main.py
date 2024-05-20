import socket
from random import choice
from threading import Thread
from constantes import HOST_DEFECTO, PORT_DEFECTO, SIZE_BUFFER

# Usamos nuestras constantes
host = HOST_DEFECTO
port = PORT_DEFECTO

# Creamos el socket, hacemos bind y listen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()


# Función encargada de escuchar a 1 cliente
def escuchar_cliente(socket_cliente: socket.socket) -> None:
    while True:
        try:
            mensaje = socket_cliente.recv(SIZE_BUFFER).decode("utf-8")
            if mensaje == "palabra":
                respuesta = choice(["Hola", "Buenos días", "Buenas Tardes"])
            else:  # mensaje == "color"
                respuesta = choice(["Rojo", "Azul", "Magenta"])
            socket_cliente.send(respuesta.encode("utf-8"))

        except Exception:
            # Ante cualquier error, se acaba la conexión
            # En este caso, se termina el thread que mantenía la conexión
            # con el socket de un cliente
            return


if __name__ == "__main__":
    counter = 0
    while counter < 5:
        try:
            print("Esperando que alguien se quiera conectar...")
            # Aceptamos a un cliente
            socket_cliente, address = sock.accept()
            print("Conexión aceptada desde", address)

            # Creamos un thread encargado de escuchar a ese cliente
            thread = Thread(target=escuchar_cliente,
                            args=(socket_cliente,), daemon=True)
            thread.start()
            counter += 1
        except ConnectionError:
            print("Ocurrió un error.")

    sock.close()
