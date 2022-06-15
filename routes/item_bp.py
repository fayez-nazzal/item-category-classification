from flask import Blueprint
from controllers.ItemController import predict_category, is_correct

item_bp = Blueprint('item_bp', __name__)
item_bp.route('/', methods=['GET'])(predict_category)
item_bp.route('/iscorrect', methods=['POST'])(is_correct)
