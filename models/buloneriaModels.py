from utils.db import db


class Producto(db.Model):
    # Define tu modelo SQLAlchemy aquí
    id = db.Column(db.Integer, primary_key=True)  # define los campos de la tabla
    cantidad = db.Column(db.Integer)
    id_categoria = db.Column(db.String(20))
    codigo = db.Column(db.Integer)
    descripcion = db.Column(db.String(50))
    precioUnit=db.Column(db.Float(precision=2))
    precioVPublico=db.Column(db.Float(precision=2))

    def __init__(
        self, cantidad, id_categoria, codigo, descripcion, precioUnit, precioVPublico
    ):  # crea el  constructor de la clase
        self.cantidad = cantidad  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.id_categoria= id_categoria
        self.codigo = codigo
        self.descripcion = descripcion
        self.precioUnit = precioUnit
        self.precioVPublico = precioVPublico

class Categoria(db.Model):
    # Define tu modelo SQLAlchemy aquí
    id = db.Column(db.Integer, primary_key=True)  # define los campos de la tabla
    catNombre = db.Column(db.String(50))

    def __init__(self, catNombre):  # crea el  constructor de la clase
        self.catNombre = catNombre  # no hace falta el id porque lo crea sola mysql por ser auto_incremento
