from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .whisper_wrapper import WhisperWrapper
from .mixtral_wrapper import MixtralWrapper
from .database import db
from .data_models import Feedback

app = Flask(__name__)
CORS(app)

# Initialize SQLite db 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
  db.create_all()

# Initialize wrappers instances for use across the app
whisper_wrapper = WhisperWrapper()
mixtral_wrapper = MixtralWrapper()

# Import routes to ensure they're registered with the Flask app instance
from app import routes
