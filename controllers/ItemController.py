from flask import request
from models.Item import Item, items
from flask_sqlalchemy import SQLAlchemy
from joblib import load
from flask import request
import pandas as pd

# Load the trained model file
clf = load('ml/svm_model.joblib')

db = SQLAlchemy()
def predict_category():
    item_name = request.args.get('item_name')
    x = pd.DataFrame([item_name])
    x.columns = ['item_name']
    
    result = clf.predict(x)[0]
    
    return result, 200

def is_correct():
    raw_item = request.get_json()
    
    item = Item(**raw_item)
    
    items.insert_one(item.to_dict())
    
    return 'success', 200
