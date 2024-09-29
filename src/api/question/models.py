from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    template_test_id = db.Column(db.String(36), db.ForeignKey('template_test.id'), nullable=False)
    
    def __init__(self, content, template_test_id):
        self.id = str(uuid4())
        self.content = content
        self.template_test_id = template_test_id