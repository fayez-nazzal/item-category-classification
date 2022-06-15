from bson import ObjectId
from pydantic import BaseModel, Field
from models.db import db

items = db['items']

class Item(BaseModel):
    item_name: str
    item_category: str
    correct: bool

    def to_dict(self):
        return {
            'item_name': self.item_name,
            'item_category': self.item_category,
            'correct': self.correct
        }
