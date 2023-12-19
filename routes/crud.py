from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.buloneriaModels import Producto
from utils.db import db
crud=Blueprint('crud',__name__)


@crud.route("/")
def index():
    # Obtén los datos de la tabla
    data = Producto.query.all()
    return render_template("index.html", data=data)

###################################################################

@crud.route("/editar/<int:id>", methods=["POST", "GET"])
def editar(id):
    item = Producto.query.get(id)
    if request.method == "POST":
        item.cantidad = request.form.get("cantidad")
        item.id_categoria = request.form.get("id_categoria")
        item.codigo = request.form.get("codigo")
        item.descripcion = request.form.get("descripcion")
        item.precioUnit = request.form.get("precioUnit")
        item.precioVPublico = request.form.get("precioVPublico")
        db.session.commit()  # confirma el alta
        return redirect(url_for("/index"))
    # Obtén los datos del elemento con el ID proporcionado
    #return render_template("editar.html", item=item)
    return render_template("crud.editar", item=item)

###################################################################

@crud.route("/nuevo", methods=["POST", "GET"])  # crea ruta o endpoint
def nuevo():
    if (
        request.method == "POST"
    ):  # print(request.json)  # request.json contiene el json que envio el cliente
        cantidad = request.form.get("cantidad")
        id_categoria = request.form.get("id_categoria")
        codigo = request.form.get("codigo")
        descripcion = request.form.get("descripcion")
        precioUnit = request.form.get("precioUnit")
        precioVPublico = request.form.get("precioVPublico")
        productoNuevo = Producto(
            cantidad, id_categoria, codigo, descripcion, precioUnit, precioVPublico
        )
        db.session.add(productoNuevo)
        db.session.commit()  # confirma el alta
        return redirect(url_for("crud.index"))
    return render_template("nuevo.html")

###################################################################

@crud.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    item = db.session.query(Producto).get(id)
    #if request.method == "POST":
    db.session.delete(item)
    db.session.commit()
    flash("Elemento eliminado correctamente", "success")
    return redirect(url_for("crud.index"))
   #return redirect(url_for("crud.index"))
