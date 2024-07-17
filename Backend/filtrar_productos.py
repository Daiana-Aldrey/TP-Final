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
                'plan de financiamiento': producto.financiacion if hasattr(producto, 'financiacion') else None,
                'descripcion': producto.descripcion,
                'imagen': producto.imagen_url
            }
            listado_de_productos.append(producto_info)

        return jsonify(listado_de_productos), 200

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500


"""def filtrar_productos_por_marca(modelo, marca):
    try:
        listado_de_productos = []
        productos = modelo.query.filter_by(marca=marca).all()
        for producto in productos:
            producto_info = {
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
                'plan de financiamiento': producto.financiacion,
                'descripcion': producto.descripcion,
                'imagen': producto.imagen_url
            }
            listado_de_productos.append(producto_info)

        return jsonify(listado_de_productos), 200

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500


def filtrar_notebooks_por_marca(marca):
    try:
        listado_de_productos = []
        notebooks = Notebook.query.filter_by(marca=marca).all()
        for notebook in notebooks:
            notebook_info = {
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
                'plan de financiamiento': notebook.financiacion,
                'descripcion': notebook.descripcion,
                'imagen': notebook.imagen_url
            }
            listado_de_productos.append(notebook_info)

        return jsonify(listado_de_productos), 200

    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500
"""

def filtrar_producto_por_id(id_producto, tabla_perteneciente):
    try:
        producto = tabla_perteneciente.query.get(id_producto)
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
            'plan de financiamiento': producto.financiacion,
            'descripcion': producto.descripcion,
            'imagen': producto.imagen_url
            }
        return jsonify(producto_informacion)
        
    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500    

def filtrar_notebook_por_id(id_notebook):
    try:
        notebook = Notebook.query.get(id_notebook)
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
            'plan de financiamiento': notebook.financiacion,
            'descripcion': notebook.descripcion,
            'imagen': notebook.imagen_url
        }

        return jsonify(notebook_informacion)
        
    except Exception as e:
        return jsonify(f"Error al intentar mostrar los productos: {str(e)}"), 500        
