from flask import Flask
from firebase_admin import credentials, firestore, initialize_app

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("SmartCafeAPI/api/serviceAccountKey.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'

    from .userAPI import userAPI

    app.register_blueprint(userAPI, url_prefix='/user')

    return app