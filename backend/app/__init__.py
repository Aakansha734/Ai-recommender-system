from flask import Flask
from flask_pymongo import PyMongo

mongo = None

def create_app():
    app = Flask(__name__)

    # MongoDB connection string
    app.config["MONGO_URI"] = "mongodb://localhost:27017/ai_recommender_db"
    global mongo
    mongo = PyMongo(app)

    # Import routes and register blueprints
    from app.routes import api
    app.register_blueprint(api)

    return app
