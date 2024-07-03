from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular,Tablet, Notebook, Plan
from filtrar_productos import filtrar_productos_por_marca, filtrar_notebooks_por_marca, filtrar_producto_por_id, filtrar_notebook_por_id

SAMSUNG = "Samsung"
APPLE = "Apple"
XIAOMI = "Xiaomi"

app = Flask(__name__)
CORS(app) #donde esta el entorno virtual intalar -> pip install flask-cors para que funcione todo 

port = 5000
#conecto la base de datos //usario_bd:contraseña@localhost:5432/nombre_bd
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:1215308@localhost:5432/tienda_online' 
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:postgres@localhost:5432/tienda_online'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route("/samsung/celulares/")
def celulares_samsung():
    return filtrar_productos_por_marca(Celular, SAMSUNG)

@app.route("/samsung/tablets/")
def tablets_samsung():
    return filtrar_productos_por_marca(Tablet, SAMSUNG)

@app.route("/samsung/notebooks/")
def notebooks_samsung():
    return filtrar_notebooks_por_marca(SAMSUNG)    

@app.route("/apple/celulares/")
def celulares_apple():
    return filtrar_productos_por_marca(Celular, APPLE)

@app.route("/apple/tablets/")
def tablets_apple():
    return filtrar_productos_por_marca(Tablet, APPLE)

@app.route("/apple/notebooks/")
def notebooks_apple():
    return filtrar_notebooks_por_marca(APPLE)    

@app.route("/xiaomi/celulares/")
def celulares_sxiaomi():
    return filtrar_productos_por_marca(Celular, XIAOMI)

@app.route("/xiaomi/tablets/")
def tablets_xiaomi():
    return filtrar_productos_por_marca(Tablet, XIAOMI)

@app.route("/xiaomi/notebooks/")
def notebooks_xiaomi():
    return filtrar_notebooks_por_marca(XIAOMI)     






      




"""
@app.route("/celulares/") #muestra todos los celulares
def celulares():
    try:
        celulares = Celular.query.all()
        listado_de_productos = []
        for celular in celulares:
            celular_informacion = {
            'id': celular.id,
            'marca': celular.marca,
            'modelo': celular.modelo,
            'procesador' : celular.procesador,
            'memoria' : celular.memoria,
            'camara delantera': celular.camara_delantera,
            'camara trasera' : celular.camara_trasera,
            'bateria' : celular.bateria,
            'pantalla' : celular.pantalla,
            'precio': celular.precio,
            'plan de financiamiento': celular.financiacion,
            'descripcion': celular.descripcion,
            'imagen': celular.imagen_url
            }

            listado_de_productos.append(celular_informacion)

        return jsonify(listado_de_productos)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500        
 """
        

@app.route("/producto/<id_producto>/<modelo>", methods=["GET"])
def producto(id_producto, modelo):
    try:
        # Busca el producto por modelo en las tres tablas
        celular = Celular.query.filter_by(modelo=modelo).first()
        tablet = Tablet.query.filter_by(modelo=modelo).first()
        notebook = Notebook.query.filter_by(modelo=modelo).first()

        # Si se encuentra el producto en alguna de las tablas
        if celular or tablet or notebook:
            # Obtiene el ID del producto encontrado
            producto_id = celular.id if celular else tablet.id if tablet else notebook.id

            # Determina la tabla a la que pertenece el producto
            tabla_perteneciente = Celular if celular else Tablet if tablet else Notebook

            # Busca el producto por ID y muestra la información
            if tabla_perteneciente == Celular:
                producto_informacion = filtrar_producto_por_id(producto_id, tabla_perteneciente)
            elif tabla_perteneciente == Tablet:
                producto_informacion = filtrar_producto_por_id(producto_id, tabla_perteneciente)
            else:  # Si es un notebook
                producto_informacion = filtrar_notebook_por_id(producto_id)

            return producto_informacion

        else:
            # Si no se encuentra el producto, devuelve un error
            return jsonify("Producto no encontrado"), 404

    except Exception as e:
        # Maneja cualquier error inesperado
        return jsonify(f"Error al mostrar el producto: {str(e)}"), 500




if __name__ == '__main__':
    print('Starting server...') 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host = '0.0.0.0', debug= True, port=port)       
    print('Started ...')
