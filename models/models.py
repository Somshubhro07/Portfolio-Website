from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def connect_db(app):
    db.init_app(app)

class Project(db.Model):
    __tablename__ = 'projects'  # Define the table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    technologies = db.Column(db.String(255))
    date_created = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Project {self.name}>'

class Contact(db.Model):
    __tablename__ = 'contacts'  # Define the table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Contact {self.name}>'

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Leaderboard {self.name} - {self.score}>'