from flask import Flask, render_template, jsonify
from services.generador import obtener_frase

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/frase")
def frase():
    return jsonify({"frase": obtener_frase()})

if __name__ == "__main__":
    app.run(debug=True)

