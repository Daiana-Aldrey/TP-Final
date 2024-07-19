import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usado(db.Model):
    __tablename__ = 'usados'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(20), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(500))
    precio = db.Column(db.Integer, nullable=False)
    imagen_url = db.Column(db.String(300), nullable=False)

class Plan(db.Model):
    __tablename__ = 'planes_de_financiacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    cuotas = db.Column(db.Integer, nullable=False)
    intereses = db.Column(db.String(30), nullable=False)
    celulares = db.relationship('Celular', backref='financiacion_plan', lazy=True)
    tablets = db.relationship('Tablet', backref='financiacion_plan', lazy=True)
    notebooks = db.relationship('Notebook', backref='financiacion_plan', lazy=True)

class Celular(db.Model):
    __tablename__ = 'celulares'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(30), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    procesador = db.Column(db.String(30), nullable=False)
    memoria = db.Column(db.String(30), nullable=False)
    camara_delantera = db.Column(db.String(30), nullable=False)
    camara_trasera = db.Column(db.String(30), nullable=False)
    pantalla = db.Column(db.String(30), nullable=False)
    bateria = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    financiacion = db.Column(db.Integer, db.ForeignKey('planes_de_financiacion.id'))
    imagen_url = db.Column(db.String(250), nullable=False)

class Tablet(db.Model):
    __tablename__ = 'tablets'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(30), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    procesador = db.Column(db.String(30), nullable=False)
    memoria = db.Column(db.String(30), nullable=False)
    camara_delantera = db.Column(db.String(30), nullable=False)
    camara_trasera = db.Column(db.String(30), nullable=False)
    pantalla = db.Column(db.String(30), nullable=False)
    bateria = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    financiacion = db.Column(db.Integer, db.ForeignKey('planes_de_financiacion.id'))
    imagen_url = db.Column(db.String(250), nullable=False)

class Notebook(db.Model):
    __tablename__ = 'notebooks'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(30), nullable=False)
    modelo = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    procesador = db.Column(db.String(30), nullable=False)
    memoria = db.Column(db.String(30), nullable=False)
    almacenamiento = db.Column(db.String(30), nullable=False)
    sistema_operativo = db.Column(db.String(30), nullable=False)
    camara_delantera = db.Column(db.String(30), nullable=False)
    pantalla = db.Column(db.String(30), nullable=False)
    bateria = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    financiacion = db.Column(db.Integer, db.ForeignKey('planes_de_financiacion.id'))
    imagen_url = db.Column(db.String(250), nullable=False)