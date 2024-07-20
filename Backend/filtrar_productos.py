from flask import Flask, request, jsonify
from flask_cors import CORS 
from modelos import db, Celular,Tablet, Notebook, Plan

def filtrar_productos_por_marca(modelo, marca):
    try:
        listado_de_productos = []
        productos = modelo.query.filter_by(marca=marca).all()
        for producto in productos:
            producto_info = {
                'id': producto.id,
                'marca': producto.marca,
                'modelo': producto.modelo,
                'procesador': producto.procesador if hasattr(producto, 'procesador') else None,
                'memoria': producto.memoria if hasattr(producto, 'memoria') else None,
                'camara delantera': producto.camara_delantera if hasattr(producto, 'camara_delantera') else None,
                'camara trasera': producto.camara_trasera if hasattr(producto, 'camara_trasera') else None,
                'bateria': producto.bateria if hasattr(producto, 'bateria') else None,
                'pantalla': producto.pantalla if hasattr(producto, 'pantalla') else None,
                'almacenamiento': producto.almacenamiento if hasattr(producto, 'almacenamiento') else None,
                'sistema operativo': producto.sistema_operativo if hasattr(producto, 'sistema_operativo') else None,
                'precio': producto.precio,
                'plan de financiamiento': producto.financiacion,
                'descripcion': producto.descripcion,
                'imagen': producto.imagen_url
            }
            listado_de_productos.append(producto_info)

        return jsonify(listado_de_productos), 200

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500



def filtrar_producto_por_id(id_producto, tabla_perteneciente):
    try:
        producto = tabla_perteneciente.query.get(id_producto)
        plan = Plan.query.get(producto.financiacion)

        plan_info = {
            'id': plan.id,
            'nombre': plan.nombre,
            'cuotas': plan.cuotas,
            'intereses': plan.intereses
        } if plan else None
        
        producto_informacion = {
            'id': producto.id,
            'marca': producto.marca,
            'modelo': producto.modelo,
            'procesador': producto.procesador,
            'memoria': producto.memoria,
            'camara delantera': producto.camara_delantera,
            'camara trasera': producto.camara_trasera,
            'bateria': producto.bateria,
            'pantalla': producto.pantalla,
            'precio': producto.precio,
            'plan de financiamiento':plan_info,
            'descripcion': producto.descripcion,
            'imagen': producto.imagen_url
            }
        return jsonify(producto_informacion)
        
    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500    

def filtrar_notebook_por_id(id_notebook):
    try:
        notebook = Notebook.query.get(id_notebook)
        plan = Plan.query.get(notebook.financiacion)
        plan_info = {
            'id': plan.id,
            'nombre': plan.nombre,
            'cuotas': plan.cuotas,
            'intereses': plan.intereses
        } if plan else None
        
        notebook_informacion = {
            'id': notebook.id,
            'marca': notebook.marca,
            'modelo': notebook.modelo,
            'procesador': notebook.procesador,
            'memoria': notebook.memoria,
            'almacenamiento': notebook.almacenamiento,
            'camara delantera': notebook.camara_delantera,
            'sistema operativo': notebook.sistema_operativo,
            'bateria': notebook.bateria,
            'pantalla': notebook.pantalla,
            'precio': notebook.precio,
            'plan de financiamiento': plan_info,
            'descripcion': notebook.descripcion,
            'imagen': notebook.imagen_url
        }

        return jsonify(notebook_informacion)
        
    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500        


def filtrar_productos_por_precio(precio_min, precio_max):
    try:
        productos_filtrados = []

        celulares = Celular.query.filter(Celular.precio.between(precio_min, precio_max)).all()
        tablets = Tablet.query.filter(Tablet.precio.between(precio_min, precio_max)).all()
        notebooks = Notebook.query.filter(Notebook.precio.between(precio_min, precio_max)).all()

        for celular in celulares:
            producto_info = {
                'id': celular.id,
                'marca': celular.marca,
                'modelo': celular.modelo,
                'precio': celular.precio,
                'imagen': celular.imagen_url
            }
            productos_filtrados.append(producto_info)

        for tablet in tablets:
            producto_info = {
                'id': tablet.id,
                'marca': tablet.marca,
                'modelo': tablet.modelo,
                'precio': tablet.precio,
                'imagen': tablet.imagen_url
            }
            productos_filtrados.append(producto_info)

        for notebook in notebooks:
            producto_info = {
                'id': notebook.id,
                'marca': notebook.marca,
                'modelo': notebook.modelo,
                'precio': notebook.precio,
                'imagen': notebook.imagen_url
            }
            productos_filtrados.append(producto_info)

        return productos_filtrados

    except Exception as e:
        print(f"Error al filtrar productos por precio: {str(e)}")
        return None

def filtrar_por_cuotas(min_cuotas, max_cuotas):
    try:
        productos_filtrados = []

        # Filtrar celulares por cuotas de financiamiento
        celulares = db.session.query(Celular, Plan.cuotas).join(Plan, Celular.financiacion == Plan.id).filter(Plan.cuotas.between(min_cuotas, max_cuotas)).all()

        for celular, cuotas in celulares:
            producto_info = {
                'id': celular.id,
                'marca': celular.marca,
                'modelo': celular.modelo,
                'precio': celular.precio,
                'imagen': celular.imagen_url,
                'cuotas': cuotas,
            }
            productos_filtrados.append(producto_info)

        # Filtrar tablets por cuotas de financiamiento
        tablets = db.session.query(Tablet, Plan.cuotas).join(Plan, Tablet.financiacion == Plan.id).filter(Plan.cuotas.between(min_cuotas, max_cuotas)).all()

        for tablet, cuotas in tablets:
            producto_info = {
                'id': tablet.id,
                'marca': tablet.marca,
                'modelo': tablet.modelo,
                'precio': tablet.precio,
                'imagen': tablet.imagen_url,
                'cuotas': cuotas,
            }
            productos_filtrados.append(producto_info)

        # Filtrar notebooks por cuotas de financiamiento
        notebooks = db.session.query(Notebook, Plan.cuotas).join(Plan, Notebook.financiacion == Plan.id).filter(Plan.cuotas.between(min_cuotas, max_cuotas)).all()

        for notebook, cuotas in notebooks:
            producto_info = {
                'id': notebook.id,
                'marca': notebook.marca,
                'modelo': notebook.modelo,
                'precio': notebook.precio,
                'imagen': notebook.imagen_url,
                'cuotas': cuotas,
            }
            productos_filtrados.append(producto_info)
        return productos_filtrados

    except Exception as e:
        print(f"Error al filtrar productos por precio: {str(e)}")
        return None