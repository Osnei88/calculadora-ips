
from flask import Flask, request, jsonify, render_template
from calculadora import calcular_ip

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/api/calcular", methods=["GET"])
def api_calcular():

    ip_digitado = request.args.get("ip", "").strip()

    if not ip_digitado:
        return jsonify({
            "erro": "Informe um IP com CIDR. Exemplo: 172.45.60.116/21"
        }), 400

    try:
        resultado = calcular_ip(ip_digitado)
        return jsonify(resultado)

    except ValueError:
        return jsonify({
            "erro": "Endereço IPv4 ou máscara CIDR inválida."
        }), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
