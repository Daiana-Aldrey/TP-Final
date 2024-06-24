from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular, Plan

app = Flask(__name__)
CORS(app) #donde esta el entorno virtual intalar -> pip install flask-cors para que funcione todo 

port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:informatico2027.@localhost:5432/tienda_online' #conecto la base de datos //usario_bd:contraseña@localhost:5432/nombre_bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'

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
            'bateria' : celular.baterias,
            'precio': celular.precio,
            'plan de financiacion': celular.financiamiento,
            'descripcion': celular.descripcion,
            'imagen': vehiculo.imagen_url
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
