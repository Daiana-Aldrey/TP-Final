from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular,Tablet, Notebook, Plan
from filtrar_productos import filtrar_productos_por_marca, filtrar_notebooks_por_marca

SAMSUNG = "Samsung"
APPLE = "Apple"
XIAOMI = "Xiaomi"

app = Flask(__name__)
CORS(app) #donde esta el entorno virtual intalar -> pip install flask-cors para que funcione todo 

port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:postgres@localhost:5432/tienda_online' #conecto la base de datos //usario_bd:contraseña@localhost:5432/nombre_bd
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
 
        

@app.route("/celulares/<id_celular>", methods=["GET"]) #Se obtiene el celular con el id dado
def celular(id_celular):
    try:
        celular = Celular.query.get(id_celular)
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

        return jsonify(celular_informacion)
    except:
        return jsonify("Lo buscado no es un producto que este a la venta"), 400




if __name__ == '__main__':
    print('Starting server...') 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host = '0.0.0.0', debug= True, port=port)       
    print('Started ...')
