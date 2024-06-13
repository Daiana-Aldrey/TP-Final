import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conejo(db.Model):
    __tablename__ = 'conejos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String[255], nullable=False)
    plata = db.Column(db.Integer, nullable= False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())


class TipoGranja(db.Model):
    __tablename__ = 'tipos_granja'
    id = db.Column(db.Integer, primary_key = True)
    verdura = db.Column(db.String[255], nullable=False)
    plata = db.Column(db.Integer, nullable= False)
    tiempo_cosecha = db.Column(db.String[255], nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())

class Granja(db.Model):
    __tablename__ = 'granjas'
    id = db.Column(db.Integer, primary_key = True)
    conejo_id = db.Column(db.Integer, db.ForeignKey('conejos.id'))
    tipo_granja_id = db.Column(db.Integer, db.ForeignKey('tipos_granja.id'))
    fecha_cosecha = db.Column(db.DateTime, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())

#nullable = False, no acepta que se ingrese caracter vacio







