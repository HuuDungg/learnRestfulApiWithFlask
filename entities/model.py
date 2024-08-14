from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref='store', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    is_activate = db.Column(db.Boolean, default=True)
    password = db.Column(db.String(80), nullable=False)
    sdt = db.Column(db.String(80), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)



    