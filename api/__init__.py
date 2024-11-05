from flask import Flask
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS, cross_origin
import firebase_admin
from firebase_admin import credentials
from .userAPI import userAPI

cred = credentials.Certificate("api/serviceAccountKey.json")
default_app = initialize_app(cred)
@cross_origin()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    
    

    app.register_blueprint(userAPI, url_prefix='/user')

    return app