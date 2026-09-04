import os
import pymysql
from flask import Flask, request

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "servidor-bd-ejemplo")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME", "legacydb")


@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        conn.close()
        return "<h1>API Legacy TechNova - Funcionando (Más o menos)</h1>"
    except Exception as e:
        return f"<h1>Sistema Caído</h1><p>{e}</p>", 500


@app.route("/buscar")
def buscar_usuario():
    usuario_id = request.args.get("id", "1")

    try:
        usuario_id = int(usuario_id)
    except ValueError:
        return "ID inválido", 400

    query_segura = f"SELECT * FROM usuarios WHERE id = {usuario_id}"

    return f"Simulando consulta: {query_segura}"


@app.route("/health")
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)