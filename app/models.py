from flask_login import UserMixin
from .extensions import db


class User(db.Model, UserMixin):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Posts', backref='user', lazy=True)

class Posts(db.Model):
    # __bind_key__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
