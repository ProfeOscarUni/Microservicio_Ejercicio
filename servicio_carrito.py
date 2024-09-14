from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carrito.db'
db = SQLAlchemy(app)

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, nullable=False)
    producto_id = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    
@app.route('/carrito', methods =['GET', 'POST'])
def carrito():
    if request.method == 'GET':
        items = Carrito.query.all()
        return jsonify([{'id': item.id, 'usuario_id':item.usuario_id, 'producto_id': item.producto_id, 'cantidad': item.cantidad} for item in items])
    elif request.method == 'POST':
        data =request.json
        nuevo_item = Carrito(usuario_id = data['usuario_id'],producto_id = data['producto_id'], cantidad = data['cantidad'])
        db.session.add(nuevo_item)
        db.session.commit()
        return jsonify({'mensaje': 'Producto agregado al carrito'}), 201
if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5002)