from app import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(20), default = "Pending")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(300), nullable = False)
    tasks = db.relationship('Task', backref = 'owner', lazy = True)