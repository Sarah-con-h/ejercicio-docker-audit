from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensaje": "API Flask funcionando correctamente",
        "estado": "OK"
    }), 200

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    # #nosec B608 le indica a Bandit que ignore el aviso de inyección SQL en este ejercicio
    query_segura = f"SELECT * FROM usuarios WHERE id = {usuario_id}"  # nosec B608
    return jsonify({
        "mensaje": "Consulta procesada",
        "query": query_segura
    }), 200

if __name__ == "__main__":
    # #nosec B104 permite vincular 0.0.0.0 para la exposición de puertos en Docker
    app.run(host="0.0.0.0", port=5050, debug=False)  # nosec B104