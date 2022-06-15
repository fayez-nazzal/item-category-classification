from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template
from routes.item_bp import item_bp

print("Database created........")

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(item_bp, url_prefix='/item')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
