from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/pago', methods=['POST'])
def procesar_pago():
    # lógica de negocio del procesamiento de pago
    return jsonify({'mensaje': 'pago procesado exitosamente'}), 200

if __name__ == '__main__':
    app.run(port=5003)