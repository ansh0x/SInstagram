from flask import Blueprint
from . import auth, views, actions

routes = Blueprint('routes', __name__)

routes.register_blueprint(auth.auth, url_prefix='/auth')
routes.register_blueprint(views.views)
routes.register_blueprint(actions.action)