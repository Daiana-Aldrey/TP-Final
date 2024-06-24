from flask import Flask, request, jsonify
from models import db, Conejo, Granja, TipoGranja

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:1215308@localhost:5432/base_camejo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'


#No estoy haciendo consulta a base de datos, lo que obtenga en la url lo toma como id_conejo
@app.route("/conejos/<id_conejo>", methods=["GET"])    
def conejo(id_conejo):
    #1conejo = Conejo.query.where(Conejo.id == id_conejo).first()  #el where no sabe que estoy buscando por id, si pongo .all() me devuelve una lista,
    #2conejo = Conejo.query.get(id_conejo) #puedo usar .get(id_conejo) que si busca por id, pero si el conejo no existe devuelve none y se rompe el servidor
    #3conejo = Conejo.query.get_or_404(id_conejo) 
    #4
    try:
        conejo = Conejo.query.get(id_conejo)
        conejo_data = {
            'id': conejo.id,
            'nombre': conejo.nombre,
            'plata': conejo.plata
        }
        return jsonify(conejo_data)
    except:
        return jsonify("El conejo no existe"), 204

@app.route("/conejos/", methods=["GET"])    
def conejos():
    try:
        conejos = Conejo.query.all()
        conejos_data = []
        for conejo in conejos:
            conejo_data = {
                'id': conejo.id,
                'nombre': conejo.nombre,
                'plata': conejo.plata
            }
            conejos_data.append(conejo_data)
        return jsonify(conejos_data)
    except:
        return jsonify("No hay conejos"), 204        


@app.route("/conejos", methods=["POST"])    
def nuevo_conejo():
    try:
        data = request.json #guarda la data que vienen en el body
        nuevo_nombre = data.get('nombre')
        plata_inicial = data.get('plata')
        nuevo_conejo = Conejo(nombre=nuevo_nombre, plata=plata_inicial) #creo nueva entidad de conejo, alchemy se encarga de poner el id incremental
        db.session.add(nuevo_conejo) #guarda el nuevo conejo en la base de datos
        ds.session.commit() #confirma la operacion
           
        return jsonify({'conejo': {'id': nuevo_conejo.id, 'nombre': nuevo_conejo.nombre, 'plata': nuevo_conejo.plata}})
    except:
        return jsonify("No se pudo creear el conejo"), 500    



if __name__ == '__main__':
    print('Starting server...') 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host = '0.0.0.0', debug= True, port=port)       
    print('Started ...')