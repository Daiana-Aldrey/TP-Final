from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular,Tablet, Notebook, Plan, Usado
from filtrar_productos import *

SAMSUNG = "Samsung"
APPLE = "Apple"
XIAOMI = "Xiaomi"

app = Flask(__name__)
CORS(app) #donde esta el entorno virtual intalar -> pip install flask-cors para que funcione todo 

port = 5000
#conecto la base de datos //usario_bd:contraseña@localhost:5432/nombre_bd
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:1215308@localhost:5432/tienda_online' 
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:postgres@localhost:5432/tienda_online'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route("/comprar/<nombre>")
def mostrar_productos(nombre):
    try:
        if nombre == 'Celular':
            productos= Celular.query.all()
        elif nombre == 'Tablet':
            productos = Tablet.query.all()
        elif nombre == 'Notebook':
            productos = Notebook.query.all()
        elif nombre == 'Usado' :
            productos = Usado.query.all()
    
        listado_de_productos = []
        for producto in productos:
            producto_informacion = {
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'precio': producto.precio,
                'imagen': producto.imagen_url
            }

            listado_de_productos.append(producto_informacion)
        return jsonify(listado_de_productos)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500     


@app.route("/comprar/<nombre>/<marca>")
def filtrar_por_marca(nombre, marca):
    try:
        if nombre == 'Celular':
            productos= Celular.query.filter_by(marca=marca).all()
        elif nombre == 'Tablet':
            productos = Tablet.query.filter_by(marca=marca).all()
        elif nombre == 'Notebook':
            productos = Notebook.query.filter_by(marca=marca).all()
        
        listado_de_productos = []
        for producto in productos:
            producto_informacion = {
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'precio': producto.precio,
                'imagen': producto.imagen_url
            }

            listado_de_productos.append(producto_informacion)
        return jsonify(listado_de_productos)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500     

@app.route("/<marca>/celulares", methods=['GET'])
def filtrar_celulares(marca):
    return filtrar_productos_por_marca(Celular, marca)

@app.route("/<marca>/tablets", methods=['GET'])
def filtrar_tablets(marca):
    return filtrar_productos_por_marca(Tablet, marca)    

@app.route("/<marca>/notebooks", methods=['GET'])
def filtrar_notebooks(marca):
    return filtrar_productos_por_marca(Notebook, marca)


@app.route("/producto/<id_producto>/<modelo>", methods=["GET"])
def producto(id_producto, modelo):
    try:
        # Busca el producto por modelo en las tres tablas
        celular = Celular.query.filter_by(modelo=modelo).first()
        tablet = Tablet.query.filter_by(modelo=modelo).first()
        notebook = Notebook.query.filter_by(modelo=modelo).first()
        usado = Usado.query.filter_by(modelo=modelo).first()

        # Si se encuentra el producto en alguna de las tablas
        if celular or tablet or notebook or usado:
            # Obtiene el ID del producto encontrado
            producto_id = celular.id if celular else tablet.id if tablet else notebook.id if notebook else usado.id

            # Determina la tabla a la que pertenece el producto
            tabla_perteneciente = Celular if celular else Tablet if tablet else Notebook if notebook else Usado

            # Busca el producto por ID y muestra la información
            if tabla_perteneciente == Celular:
                producto_informacion = filtrar_producto_por_id(producto_id, tabla_perteneciente)
            elif tabla_perteneciente == Tablet:
                producto_informacion = filtrar_producto_por_id(producto_id, tabla_perteneciente)
            elif tabla_perteneciente == Notebook:  # Si es un notebook
                producto_informacion = filtrar_notebook_por_id(producto_id)
            else:
                producto_informacion = filtrar_usados_por_id(producto_id)

            return producto_informacion

        else:
            # Si no se encuentra el producto, devuelve un error
            return jsonify("Producto no encontrado"), 404

    except Exception as e:
        # Maneja cualquier error inesperado
        return jsonify(f"Error al mostrar el producto: {str(e)}"), 500    
  

@app.route("/celulares/") #muestra todos los celulares
def celulares():
    try:
        listado_de_productos = []
        lista= [Celular, Tablet, Notebook]
        for clase in lista:
            productos= clase.query.filter_by(financiacion=4).all()

            for producto in productos:
                producto_informacion = {
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'imagen': producto.imagen_url
                }

                listado_de_productos.append(producto_informacion)

        return jsonify(listado_de_productos)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500        

@app.route('/productos', methods=['POST'])
def crear_producto():
    try:
        data = request.json
        categoria = data['categoria']
        marca = data['marca']
        modelo = data['modelo']
        descripcion = data['descripcion']
        precio = data['precio']
        imagen_url = data['imagen_url']
        nuevo_producto = Usado(categoria=categoria, modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, imagen_url=imagen_url)
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'id': nuevo_producto.id, 'modelo': nuevo_producto.modelo, 'marca': nuevo_producto.marca, 'descripcion': nuevo_producto.descripcion, 'precio': nuevo_producto.precio, 'imagen_url': imagen_url}), 201
    except Exception as e:
        return jsonify(f"Error al crear el producto: {str(e)}"), 500

@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        productos = Usado.query.all()
        listado_productos = []
        for producto in productos:
            producto_info = {
                'id': producto.id,
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': producto.precio,
                'imagen_url': producto.imagen_url
            }
            listado_productos.append(producto_info)
        return jsonify(listado_productos)
    except Exception as e:
        return jsonify(f"Error al obtener los productos: {str(e)}"), 500
    
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto_por_id(id):
    try:
        producto = Usado.query.get(id)
        if not producto:
            return jsonify('Producto no encontrado'), 404

        producto_info = {
            'id': producto.id,
            'categoria': producto.categoria,
            'marca': producto.marca,
            'modelo': producto.modelo,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'imagen_url': producto.imagen_url
        }
        return jsonify(producto_info)
    except Exception as e:
        return jsonify(f"Error al obtener el producto: {str(e)}"), 500

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        producto = Usado.query.get(id)
        if not producto:
            return jsonify('Producto no encontrado'), 404

        data = request.json
        producto.categoria = data['categoria']
        producto.marca = data['marca']
        producto.modelo = data['modelo']
        producto.descripcion = data['descripcion']
        producto.precio = data['precio']
        producto.imagen_url = data['imagen_url']

        db.session.commit()
        return jsonify({'mensaje': 'Producto actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify(f"Error al actualizar el producto: {str(e)}"), 500

@app.route('/productos/<int:id>', methods=['DELETE'])
def borrar_producto(id):
    try:
        producto = Usado.query.get(id)
        if not producto:
            return jsonify('Producto no encontrado'), 404

        db.session.delete(producto)
        db.session.commit()
        return jsonify({'mensaje': 'Producto eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify(f"Error al eliminar el producto: {str(e)}"), 500





if __name__ == '__main__':
    print('Starting server...') 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host = '0.0.0.0', debug= True, port=port)       
    print('Started ...')
