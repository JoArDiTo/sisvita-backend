from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Test(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.String(36), primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    clasification_id = db.Column(db.String(36), db.ForeignKey('clasification.id'), nullable=False)
    template_test_id = db.Column(db.String(36), db.ForeignKey('template_test.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    
    answer = db.relationship('Answer', backref='test', cascade='all, delete-orphan', lazy=True)
    
    def __init__(self, score, clasification_id, template_test_id, user_id):
        self.id = str(uuid4())
        self.score = score
        self.date = datetime.now(timezone(timedelta(hours=-5)))
        self.clasification_id = clasification_id
        self.template_test_id = template_test_id
        self.user_id = user_id