from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Clasification(db.Model):
    __tablename__ = 'clasification'
    
    id = db.Column(db.String(36), primary_key=True)
    min_score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    interpretation = db.Column(db.String(255), nullable=False)
    template_test_id = db.Column(db.String(36), db.ForeignKey('template_test.id'), nullable=False)
    
    test = db.relationship('Test', backref='clasification',cascade='all, delete-orphan', lazy=True)
    
    def __init__(self, min_score, max_score, interpretation, template_test_id):
        self.id = str(uuid4())
        self.min_score = min_score
        self.max_score = max_score
        self.interpretation = interpretation
        self.template_test_id = template_test_id