from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Alternative(db.Model):
    __tablename__ = 'alternative'

    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    template_test_id = db.Column(db.String(36), db.ForeignKey('template_test.id'), nullable=False)
    
    def __init__(self, content, value, template_test_id):
        self.id = str(uuid4())
        self.content = content
        self.value = value
        self.template_test_id = template_test_id