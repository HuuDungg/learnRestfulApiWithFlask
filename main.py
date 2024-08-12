from flask import Flask, jsonify
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

@app.route("/getAllItems", methods=['GET'])
def getAllItems():
    items = Item.query.all()
    # Chuyển đổi đối tượng Item thành danh sách các dictionary
    items_list = [
        {
        'id': item.id,
         'name': item.name, 
         'price': item.price, 
         'store_id': item.store_id
         }
           for item in items
    ]
    return jsonify(items_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
