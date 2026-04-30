from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Función para cargar respuestas desde el JSON
def cargar_respuestas():
    with open('datos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/chat', methods=['GET'])
def chat():
    # Obtenemos la pregunta de la URL, ej: /chat?pregunta=hola
    pregunta = request.args.get('pregunta', '').lower()
    respuestas = cargar_respuestas()
    
    # Buscamos la respuesta o damos una por defecto
    respuesta = respuestas.get(pregunta, "Lo siento, no entiendo esa pregunta.")
    
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000 y accesible desde cualquier IP (0.0.0.0)
    # Esto es vital para que Docker funcione luego
    app.run(host='0.0.0.0', port=5000)
