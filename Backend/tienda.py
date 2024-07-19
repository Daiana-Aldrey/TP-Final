from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular, Tablet, Notebook, Plan

app = Flask(__name__)
CORS(app)  

port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://juan:juan@localhost/tienda_online'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/productos/<tipo>", methods=["GET"])
def productos(tipo):
    try:
        if tipo == 'celulares':
            productos = Celular.query.all()
        elif tipo == 'tablets':
            productos = Tablet.query.all()
        elif tipo == 'notebooks':
            productos = Notebook.query.all()
        else:
            return jsonify("Tipo de producto no válido"), 400
        
        listado_de_productos = []
        for producto in productos:
            producto_info = {
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'descripcion': producto.descripcion,
                'procesador': producto.procesador,
                'memoria': producto.memoria,
                'camara_delantera': producto.camara_delantera,
                'camara_trasera': producto.camara_trasera,
                'pantalla': producto.pantalla,
                'bateria': producto.bateria,
                'precio': producto.precio,
                'financiacion': {
                    'nombre': producto.financiacion_plan.nombre,
                    'cuotas': producto.financiacion_plan.cuotas,
                    'intereses': producto.financiacion_plan.intereses
                } if producto.financiacion_plan else None,
                'imagen': producto.imagen_url
            }
            listado_de_productos.append(producto_info)
        return jsonify(listado_de_productos)
    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500

@app.route("/productos/<tipo>/<int:id_producto>", methods=["GET"])
def producto_por_id(tipo, id_producto):
    try:
        if tipo == 'celulares':
            producto = Celular.query.get(id_producto)
        elif tipo == 'tablets':
            producto = Tablet.query.get(id_producto)
        elif tipo == 'notebooks':
            producto = Notebook.query.get(id_producto)
        else:
            return jsonify("Tipo de producto no válido"), 400

        if not producto:
            return jsonify("Producto no encontrado"), 404

        producto_info = {
            'id': producto.id,
            'marca': producto.marca,
            'modelo': producto.modelo,
            'descripcion': producto.descripcion,
            'procesador': producto.procesador,
            'memoria': producto.memoria,
            'camara_delantera': producto.camara_delantera,
            'camara_trasera': producto.camara_trasera,
            'pantalla': producto.pantalla,
            'bateria': producto.bateria,
            'precio': producto.precio,
            'financiacion': {
                'nombre': producto.financiacion_plan.nombre,
                'cuotas': producto.financiacion_plan.cuotas,
                'intereses': producto.financiacion_plan.intereses
            } if producto.financiacion_plan else None,
            'imagen': producto.imagen_url
        }

        return jsonify(producto_info)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar el producto: {str(e)}"), 500


@app.route('/planes_financiamiento', methods=['GET'])
def planes_financiamiento():
    try:
        planes = Plan.query.all()

        listado_planes = []
        for plan in planes:
            plan_info = {
                'id': plan.id,
                'nombre': plan.nombre,
                'cuotas': plan.cuotas,
                'intereses': plan.intereses
            }
            listado_planes.append(plan_info)

        return jsonify(listado_planes)

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los planes de financiamiento: {str(e)}"), 500
        
@app.route('/disponibilidad/<categoria>', methods=['GET'])
def disponibilidad(categoria):
    try:
        if categoria == 'celular':
            productos = Celular.query.all()
        elif categoria == 'tablet':
            productos = Tablet.query.all()
        elif categoria == 'computador':
            productos = Computador.query.all()
        else:
            return jsonify({"error": "Categoría no válida"}), 400
        
        disponibilidad = []
        for producto in productos:
            disponibilidad.append({
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'disponible': producto.disponible
            })

        return jsonify(disponibilidad)

    except Exception as e:
        return jsonify(f"Error al obtener la disponibilidad de productos: {str(e)}"), 500

@app.route('/modelos/<categoria>/<marca>', methods=['GET'])
def obtener_modelos(categoria, marca):
    try:
        if categoria == 'celular':
            productos = Celular.query.filter_by(marca=marca).all()
        elif categoria == 'tablet':
            productos = Tablet.query.filter_by(marca=marca).all()
        elif categoria == 'notebook':
            productos = Notebook.query.filter_by(marca=marca).all()
        else:
            return jsonify({"error": "Categoría no válida"}), 400
        
        modelos = []
        for producto in productos:
            modelos.append(producto.modelo)

        return jsonify({"modelos": modelos})
    except Exception as e:
        return jsonify(f"Error al obtener los modelos: {str(e)}"), 500

@app.route('/categorias/<categoria>', methods=['GET'])
def obtener_marcas(categoria):
    try:
        if categoria == 'celular':
            productos = Celular.query.all()
        elif categoria == 'tablet':
            productos = Tablet.query.all()
        elif categoria == 'laptop':
            productos = Notebook.query.all()
        else:
            return jsonify({"error": "Categoría no válida"}), 400

        marcas = set()
        for producto in productos:
            marcas.add(producto.marca)

        return jsonify({"marcas": list(marcas)})

    except Exception as e:
        return jsonify({"error": f"Error al obtener marcas: {str(e)}"}), 500

if __name__ == '__main__':
    print('Starting server...') 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started ...')