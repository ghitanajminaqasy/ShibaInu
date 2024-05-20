from flask import Flask
from . import db

class PendinginRuangan(db.Model):
    __tablename__ = 'pendingin_ruangan'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'status': self.status
        }

# Initializing Flask app and SQLAlchemy
def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pendingin_ruangan.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
