from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Answer(db.Model):
    __tablename__ = 'answer'
    
    id = db.Column(db.String(36), primary_key=True)
    test_id = db.Column(db.String(36), db.ForeignKey('test.id'), nullable=False)
    question_id = db.Column(db.String(36), db.ForeignKey('question.id'), nullable=False)
    alternative_id = db.Column(db.String(36), db.ForeignKey('alternative.id'), nullable=False)
    
    def __init__(self, test_id, question_id, alternative_id):
        self.id = str(uuid4())
        self.test_id = test_id
        self.question_id = question_id
        self.alternative_id = alternative_id