from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)


def init_db():
    with app.app_context():
        db.create_all()
        # Agregar algunos productos de ejemplo
        if not Producto.query.first():
            productos = [
                Producto(nombre='Lavadora', precio=499.99),
                Producto(nombre='Refrigerador', precio=799.99),
                Producto(nombre='Microondas', precio=99.99),
                Producto(nombre='Licuadora', precio=49.99),
                Producto(nombre='Horno eléctrico', precio=199.99)
            ]
            db.session.add_all(productos)
            db.session.commit()
            print("Base de datos inicializada con productos de ejemplo.")
        else:
            print("La base de datos ya contiene productos.")


if __name__ == '__main__':
    init_db()
