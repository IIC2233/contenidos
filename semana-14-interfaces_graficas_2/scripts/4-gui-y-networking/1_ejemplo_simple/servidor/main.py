import socket
from random import choice
from threading import Thread
from constantes import HOST_DEFECTO, PORT_DEFECTO, SALUDOS, COLORES
from protocolo import enviar, recibir


# Función encargada de escuchar a 1 cliente
def escuchar_cliente(socket_cliente: socket.socket, direccion: tuple) -> None:
    try:
        while True:
            mensaje = recibir(socket_cliente).decode("utf-8")
            print(f"[{direccion}] pidió: {mensaje}")
            if mensaje == "palabra":
                respuesta = choice(SALUDOS)
            else:  # mensaje == "color"
                respuesta = choice(COLORES)
            enviar(socket_cliente, respuesta.encode("utf-8"))

    except ConnectionError:
        # El cliente se desconectó: se termina el thread que lo atendía
        print(f"[{direccion}] se desconectó")
    finally:
        socket_cliente.close()


if __name__ == "__main__":
    # Creamos el socket, hacemos bind y listen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite reutilizar el puerto apenas se cierra el servidor. Sin esto,
    # al reiniciarlo rápido aparece "OSError: Address already in use"
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST_DEFECTO, PORT_DEFECTO))
    sock.listen()

    try:
        while True:
            print("Esperando que alguien se quiera conectar...")
            # Aceptamos a un cliente
            socket_cliente, direccion = sock.accept()
            print("Conexión aceptada desde", direccion)

            # Creamos un thread encargado de escuchar a ese cliente
            thread = Thread(
                target=escuchar_cliente, args=(socket_cliente, direccion), daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("Se hizo CTRL+C ... finalizando el programa.")

    print("Cerrando socket.")
    sock.close()
