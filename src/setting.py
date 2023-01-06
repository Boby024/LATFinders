import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

load_dotenv()

SQLALCHEMY_DATABASE_URI_PROD = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
SQLALCHEMY_DATABASE_URI_DEV = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
ENV = os.getenv('ENV')
FLASK_APP = os.getenv('FLASK_APP')
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
TESTING = os.getenv('TESTING')


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    if TESTING == "False":
        app.config['TESTING'] = False
    else:
        app.config['TESTING'] = True

    if ENV == "prod":
        app.config['ENV'] = ENV
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI_PROD
    else:
        app.config['ENV'] = ENV
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI_DEV 

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # db.session.commit()

    return app