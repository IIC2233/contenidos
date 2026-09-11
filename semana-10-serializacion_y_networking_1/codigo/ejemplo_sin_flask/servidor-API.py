"""Aplicación WSGI mínima usada por el notebook de servidor."""

import json
from wsgiref.simple_server import make_server


def json_response(start_response, status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    start_response(status, headers)
    return [body]


def application(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    routes = {
        "/": {"mensaje": "Hello World"},
        "/goodbye/": {"mensaje": "Que la fuerza esté contigo"},
    }

    if path not in routes:
        return json_response(
            start_response,
            "404 Not Found",
            {"error": "Ruta inexistente"},
        )
    if method != "GET":
        return json_response(
            start_response,
            "405 Method Not Allowed",
            {"error": "Método no permitido"},
        )

    return json_response(start_response, "200 OK", routes[path])


if __name__ == "__main__":
    with make_server("localhost", 4444, application) as servidor:
        print("Escuchando en http://localhost:4444")
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("Servidor detenido")
