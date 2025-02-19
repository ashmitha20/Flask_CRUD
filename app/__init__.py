from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from app.config import Config

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    mongo.init_app(app)
    bcrypt.init_app(app)

    from app.routes import user_routes
    app.register_blueprint(user_routes, url_prefix='/users')

    return app
