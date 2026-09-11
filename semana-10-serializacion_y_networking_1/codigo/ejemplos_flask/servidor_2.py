from flask import Flask, Response, abort, request


app = Flask(__name__)


@app.route("/hi/<string:username>", methods=["GET"])
def saludar(username):
    return {"texto": f"Hola {username}!"}


@app.route("/argumentos", methods=["GET"])
def argumentos():
    nombre = request.args.get("nombre", default="Guillermo", type=str)
    especie = request.args.get("especie", default="Gato", type=str)
    edad = request.args.get("edad", default=0, type=int)
    return {"texto": f"Hola {especie} {nombre} de {edad} años!"}


@app.route("/body", methods=["POST"])
def datos_en_body():
    body_data = request.get_json()

    if not isinstance(body_data, dict):
        return {"error": "El cuerpo debe ser un objeto JSON."}, 400
    if not {"var_1", "var_2"} <= body_data.keys():
        return {"error": "Faltan var_1 o var_2."}, 400

    numero_1 = body_data["var_1"]
    numero_2 = body_data["var_2"]
    if not isinstance(numero_1, (int, float)) or not isinstance(
        numero_2,
        (int, float),
    ):
        return {"error": "Las variables deben ser números."}, 422

    return {
        "var_1": numero_1,
        "var_2": numero_2,
        "result": numero_1 + numero_2,
    }


@app.route("/error/<int:instruccion>", methods=["DELETE"])
def error(instruccion):
    if instruccion == 0:
        abort(400)
    if instruccion == 1:
        return Response(status=418)
    if instruccion == 2:
        return Response(
            "Podemos mandar textos",
            status=200,
            content_type="text/plain; charset=utf-8",
        )
    if instruccion == 3:
        return {"mensaje": "También JSON"}
    abort(404)


if __name__ == "__main__":
    app.run(host="localhost", port=4444)
