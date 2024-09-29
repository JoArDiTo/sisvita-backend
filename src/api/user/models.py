from src.common.utils.db import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash
from uuid import uuid4

@dataclass
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36), primary_key=True)
    document_type = db.Column(db.String(10), nullable=False)
    document_number = db.Column(db.String(15), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    paternal_surname = db.Column(db.String(30), nullable=False)
    maternal_surname = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    test = db.relationship('Test', backref='user',cascade='all, delete-orphan', lazy=True)
    
    def __init__(self, document_type, document_number, first_name, paternal_surname, maternal_surname, phone_number, email, password):
        self.id = str(uuid4())
        self.document_type = document_type
        self.document_number = document_number
        self.first_name = first_name
        self.paternal_surname = paternal_surname
        self.maternal_surname = maternal_surname
        self.phone_number = phone_number
        self.email = email
        self.password = generate_password_hash(password)