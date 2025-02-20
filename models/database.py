from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connects the database to the Flask app."""
    db.init_app(app)
