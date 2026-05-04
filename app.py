from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def cargar_base_datos():
    try:
        with open("datos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"preguntas": []}

@app.route('/chat', methods=['GET'])
def chat():
    pregunta_usuario = request.args.get('pregunta', '').lower()
    base_datos = cargar_base_datos()
    
    palabras_pregunta = set(pregunta_usuario.split())
    
    # Lógica del profesor: buscar coincidencia de palabras clave
    for item in base_datos['preguntas']:
        palabras_clave = set(item['pregunta'].lower().split())
        if palabras_clave.intersection(palabras_pregunta):
            respuesta = item['respuesta']
            url = item.get('url', 'No disponible')
            return jsonify({"respuesta": f"{respuesta} Más información: {url}"})
    
    return jsonify({"respuesta": "Lo siento, no tengo una respuesta para esa pregunta."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
