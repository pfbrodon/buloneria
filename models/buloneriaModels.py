from utils.db import db


class Producto(db.Model):
    # Define tu modelo SQLAlchemy aquí
    id = db.Column(db.Integer, primary_key=True)  # define los campos de la tabla
    cantidad = db.Column(db.Integer)
    categoria_id = db.Column(db.String(50))
    codigo = db.Column(db.Integer)
    descripcion = db.Column(db.String(50))
    precioUnit = db.Column(db.Numeric(precision=10, scale=2))
    precioVPublico = db.Column(db.Numeric(precision=10, scale=2))

    def __init__(
        self, cantidad, categoria_id, codigo, descripcion, precioUnit, precioVPublico
    ):  # crea el  constructor de la clase
        self.cantidad = cantidad  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.categoria_id = categoria_id
        self.codigo = codigo
        self.descripcion = descripcion
        self.precioUnit = precioUnit
        self.precioVPublico = precioVPublico