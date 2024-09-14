from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/productos', methods=['GET'])
def productos():
    try:
        response = requests.get('http://localhost:5001/productos')
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except request.RequestException as e:
        print(f"Error al comunicarse con el servicio de productos: {e}")
        return jsonify({"error": "Error al comunicarse con el servicio de productos"}), 500

@app.route('/carrito', methods=['GET', 'POST'])
def carrito():
    if request.method == 'GET':
        response = requests.get('http://localhost:5002/carrito')
    elif request.method == 'POST':
        response = requests.post('http://localhost:5002/carrito', json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/pago', methods=['POST'])
def pago():
    response = requests.post('http://localhost:5003/pago', json=request.json)
    return jsonify(response.json()), response.status_code

if __name__=='__main__':
    app.run(port=5000)