from flask import Flask
from .extensions import db, login_maneger, migrate

def create_app():
    global app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    app.config['SECRET_KEY'] = 'Secret Key Motherfucker'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}


    from .routes import routes
    app.register_blueprint(routes)

    db.init_app(app)
    login_maneger.init_app(app)
    migrate.init_app(app=app, db=db)

    return app

