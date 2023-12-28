from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS       # del modulo flask_cors importar CORS

from flask_marshmallow import Marshmallow
from sqlalchemy import Numeric
app = Flask(__name__)
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


@app.route('/login', methods=['POST','GET'])
def login():
        if request.method == 'POST':   
            email = request.form['email']
            password = request.form['password']
        
            #usuario_autenticado = Login.query.filter_by(email=email).first()
            usuario_autenticado = Usuarios.query.filter_by(email=email, password=password).first()

            if usuario_autenticado: # and check_password_hash(usuario_autenticado.password, password):
                # Autenticación exitosa
                if usuario_autenticado.tipouser=='admin':
                    return redirect(url_for('get_ProductTabla'))
                else:
                    return redirect(url_for('get_ProductTablaCliente'))
            else:
                # Credenciales incorrectas
                return render_template('index.html', mensaje="Usuario Incorrecto")
            
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


###DEFINIMOS LA RUTA DE LA VISTA PARA EL JSON GENERADO
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
    jsonresult= jsonify(result)                                            # trae todos los registros de la tabla
    return jsonresult

###DEFINIMOS LA RUTA DE LA VISTA PARA LA TABLA DEL LOGIN DE ADMINISTRACION
@app.route('/productos/tablaadmin',methods=['GET'])
def get_ProductTabla():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
    jsonresult= jsonify(result)                                            # trae todos los registros de la tabla
    #return jsonresult
    return render_template('productosbs5admin.html', jsonresult=jsonresult )                      # retorna un JSON de todos los registros de la tabla

###DEFINIMOS LA RUTA DE LA VISTA PARA LA TABLA DEL LOGIN DE CLIENTE
@app.route('/productos/tablaclientes',methods=['GET'])
def get_ProductTablaCliente():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
    jsonresult= jsonify(result)                                            # trae todos los registros de la tabla
    #return jsonresult
    return render_template('productosbs5clientes.html', jsonresult=jsonresult )                      # retorna un JSON de todos los registros de la tabla

######DEFINIMOS LA RUTA DE LA VISTA PARA LA TABLA DE UN PRODUCTO NUEVO#########
@app.route('/productos/tablaadmin/productoNuevo', methods=['GET','POST'])
def productoNuevo():
    return render_template('productobs5Nuevo.html')

####DEFINIMOS LA RUTA DE LA VISTA PARA EL ALTA DE UN PRODUCTO########
@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    cantidad=request.json['cantidad']
    categoria=request.json['categoria']
    codigo=request.json['codigo']
    descripcion=request.json['descripcion']
    precioUnit=request.json['precioUnit']
    precioVPublico=request.json['precioVPublico']
    new_producto=Producto(cantidad,categoria,codigo,descripcion,precioUnit,precioVPublico)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)

####DEFINIMOS LA RUTA DE LA VISTA PARA EL PRODUCTO POR ID################
@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    print(producto)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro

#####DEFINIMOS LA RUTA DE ELIMINACION DE UN PRODUCTO#####################
@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


####DEFINIMOS LA RUTA PARA EL TEMPLATE DE EDICION#######################
@app.route('/productos/tablaadmin/productoEdicion/<int:id>')
def editar(id):
    # Obtén los datos del elemento con el ID proporcionado
    item = Producto.query.get(id)
    return render_template('productobs5Edicion.html', item=item)






####DEFINIMOS LA RUTA PARA LA EDICION DEL PRODUCTO
@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
 
    producto.cantidad=request.json['cantidad']
    producto.categoria=request.json['categoria']
    producto.codigo=request.json['codigo']
    producto.descripcion=request.json['descripcion']
    producto.precioUnit=request.json['precioUnit']
    producto.precioVPublico=request.json['precioVPublico']
    
    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto

###DEFINIMOS LA RUTA DE LA VISTA PARA LA TABLA DEL EDICION DE PRODUCTO
'''@app.route('/productos/tablaadmin/<id>',methods=['GET', 'POST'])
def productoEdicion(id):
    if request.method == 'POST':
        return redirect(url_for('get_ProductEdicion', id=id))
    productos=Producto.query.get(id)         # el metodo query.all() lo hereda de db.Model
    #jsonresult= jsonify(productos)                                            # trae todos los registros de la tabla
    #return jsonresult
    return render_template('productobs5Edicion.html', productos=productos )                      # retorna un JSON de todos los registros de la tabla
'''
####DEFINIMOS LA RUTA PARA EL TEMPLATE DE EDICION#######################
@app.route('/productos/tablaadmin/productoEdicion', methods=['GET','POST'])
def productoEdicion():
    return render_template('productobs5Edicion.html')


if __name__=='__main__':
    app.run(debug=True)