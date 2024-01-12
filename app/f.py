from flask import url_for
from . import app

with app.app_context():
    floder = url_for('UPLOADS_FOLDER')
    print(floder)