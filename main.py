from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import db, Item, Store
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/train06'

db.init_app(app)

@app.route('/')
def index():
    try:
        db.engine.connect()
        return "Connection successful"
    except Exception as e:
        return f"Connection failed: {e}"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
