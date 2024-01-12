from flask import Flask
from .extensions import db, login_maneger, migrate

def create_app():
    global app

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    app.config['SECRET_KEY'] = 'Secret Key Motherfucker'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}


    from .auth import auth # Impoting Authenticaton views
    app.register_blueprint(auth)

    from .main import main
    app.register_blueprint(main) # Impoting other genral views

    db.init_app(app)
    login_maneger.init_app(app)
    migrate.init_app(app=app, db=db)

    return app

#  Function to check accepted file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']