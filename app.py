from dotenv import load_dotenv
import os

load_dotenv()

from flask import Flask, send_from_directory
from routes.item_bp import item_bp

print("Database created........")

app = Flask(__name__, static_folder='client/dist')
app.config.from_object('config')

app.register_blueprint(item_bp, url_prefix='/item')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
