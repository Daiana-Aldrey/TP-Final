from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular, Tablet, Notebook, Plan
from modelos import Producto

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
    
# En tienda.py
@app.route('/productos', methods=['POST'])
def crear_producto():
    try:
        data = request.json
        nuevo_producto = Producto(
            nombre=data['nombre'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            imagen_url=data['imagen_url']
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'mensaje': 'Producto creado exitosamente'}), 201
    except Exception as e:
        return jsonify(f"Error al crear el producto: {str(e)}"), 500

@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        productos = Producto.query.all()
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
        producto = Producto.query.get(id)
        if not producto:
            return jsonify('Producto no encontrado'), 404

        producto_info = {
            'id': producto.id,
            'nombre': producto.nombre,
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
        producto = Producto.query.get(id)
        if not producto:
            return jsonify('Producto no encontrado'), 404

        data = request.json
        producto.nombre = data['nombre']
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
        producto = Producto.query.get(id)
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
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started ...')
