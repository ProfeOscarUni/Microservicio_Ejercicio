from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

def init_db():
    with app.app_context():
        db.create_all()
        if not Producto.query.first():
            productos =[
                Producto(nombre='Lavadora', precio=499.99),
                Producto(nombre='Nevera', precio=699.99),
                Producto(nombre='Microondas', precio=99.99),
            ]
            db.session.add_all(productos)
            db.session.commit()

class Producto(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([{'id':p.id, 'nombre': p.nombre, 'precio': p.precio} for p in productos])
init_db()
if __name__ =='__main__':
    app.run(port=5001)