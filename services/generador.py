import json
import random

def obtener_frase():
    with open("data/frases.json", "r", encoding="utf-8") as archivo:
        frases = json.load(archivo)

    return random.choice(frases)
