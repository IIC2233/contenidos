from flask import Flask, request

app = Flask(__name__)


# Caso 1: endpoint dinámico
@app.route("/hi/<string:username>", methods=["GET"])
def saludar(username):
    return {"texto": f"Hola {username}!"}


# Caso 2: argumentos en la URL
@app.route("/argumentos", methods=["GET"])
def argumentos():
    name = request.args.get("name", "Anya")
    surname = request.args.get("surname", "Forger")
    return {"texto": f"Hola {name} {surname}!"}


# Caso 3: datos en el body
@app.route("/body", methods=["POST"])
def datos_en_body():
    body_data = request.get_json(force=True)
    numero_1 = body_data["var_1"]
    numero_2 = body_data["var_2"]
    resultado = numero_1 + numero_2
    return {"var_1": numero_1, "var_2": numero_2, "result": resultado}


if __name__ == "__main__":
    app.run(host="localhost", port=4444)
