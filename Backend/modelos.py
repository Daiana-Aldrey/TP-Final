import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plan(db.Model):
    __tablename__ = 'planes_de_financiacion'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String[30], nullable=False)
    cuotas = db.Column(db.Integer, nullable= False)
    intereses = db.Column(db.String[30], nullable=False)

class Celular(db.Model):
    __tablename__ = 'celulares'
    id = db.Column(db.Integer, primary_key = True)
    marca = db.Column(db.String[30], nullable=False)
    modelo = db.Column(db.String[30], nullable=False)
    descripcion = db.Column(db.String[300], nullable=False)
    procesador = db.Column(db.String[30], nullable=False)
    memoria = db.Column(db.String[30], nullable=False)
    camara_delantera = db.Column(db.String[30], nullable=False)
    camara_trasera = db.Column(db.String[30], nullable=False)
    pantalla = db.Column(db.String[30], nullable=False)
    bateria = db.Column(db.String[30], nullable=False)
    precio = db.Column(db.Integer, nullable= False)
    financiacion = db.Column(db.Integer, db.ForeignKey('planes_de_financiacion.id'))
    imagen_url =db.Column(db.String[250], nullable=False)
    







