from flask_login import UserMixin
from .extensions import db

likes = db.Table('likes',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),                 
        db.Column('post_id', db.Integer, db.ForeignKey('posts.id'))                 
)

class User(db.Model, UserMixin):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Posts', backref='user', lazy=True)

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    follower = db.relationship('User', foreign_keys=[follower_id], backref=db.backref('followers', lazy=True))
    following = db.relationship('User', foreign_keys=[following_id], backref=db.backref('following', lazy=True))


class Posts(db.Model):
    # __bind_key__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String, nullable=False)
    caption = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    likes = db.relationship('User', secondary=likes, backref='liked_posts')
    comments = db.relationship('Comments', backref='post', lazy=True)

    def total_likes(self):
        return len(self.likes)

    def total_comments(self):
        return len(self.comments)

class Comments(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
