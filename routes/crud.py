from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.buloneriaModels import Producto, Categoria
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
    catnombre= Categoria.query.all()
    if request.method == "POST":
        item.cantidad = request.form.get("cantidad")
        item.id_categoria = request.form.get("catNombre")
        item.codigo = request.form.get("codigo")
        item.descripcion = request.form.get("descripcion").upper()
        item.precioUnit = request.form.get("precioUnit")
        item.precioVPublico = request.form.get("precioVPublico")
        db.session.commit()  # confirma el alta
        return redirect(url_for("crud.index"))
    # Obtén los datos del elemento con el ID proporcionado
    #return render_template("editar.html", item=item)
    return render_template("editar.html", item=item, catnombre=catnombre)

###################################################################

@crud.route("/nuevo", methods=["POST", "GET"])  # crea ruta o endpoint
def nuevo():
    catnombre= Categoria.query.all()
    if (request.method == "POST"):  
        cantidad = request.form.get("cantidad")
        id_categoria = request.form.get("catNombre")
        codigo = request.form.get("codigo")
        descripcion = request.form.get("descripcion").upper()
        precioUnit = request.form.get("precioUnit")
        precioVPublico = request.form.get("precioVPublico")
        productoNuevo = Producto(
            cantidad, id_categoria, codigo, descripcion, precioUnit, precioVPublico
        )
        db.session.add(productoNuevo)
        db.session.commit()  # confirma el alta
        return redirect(url_for("crud.index"))
    return render_template("nuevo.html", catnombre=catnombre)

###################################################################

@crud.route("/eliminar/<id>")
def eliminar(id):
    item = Producto.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect("/")
   #return redirect(url_for("crud.index"))

##################################################################

@crud.route('/lista')
def lista():
    data = Producto.query.all()
    return render_template("lista.html", data=data)

#########################################################################

@crud.route('/buscar', methods=['POST'])
def buscar():
    criterioBusqueda= request.form.get("buscar")
    print(f'EL CRITERIO DE BUSQUEDA ES: {criterioBusqueda}')
    if request.method == 'POST':
        #criterioBusq= "tornillo"
        #resultadoBusq = Producto.query.filter_by(descripcion=criterioBusq).all()
        resultadoBusqueda = Producto.query.filter(Producto.descripcion.contains(criterioBusqueda)).all()
        return render_template("index.html", data=resultadoBusqueda)
    
#########################################################################

@crud.route('/filtro', methods=['POST'])
def filtro():
    criterioFiltro= request.form.get("filtro")
    print(f'EL CRITERIO DE BUSQUEDA ES: {criterioFiltro}')
    if request.method == 'POST':
        #criterioBusq= "tornillo"
        #resultadoBusq = Producto.query.filter_by(descripcion=criterioBusq).all()
        resultadoBusqueda = Producto.query.filter(Producto.id_categoria.contains(criterioFiltro)).all()
        return render_template("index.html", data=resultadoBusqueda)