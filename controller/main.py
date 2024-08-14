import sys
import os
from flask_jwt_extended import JWTManager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from entities.model import db, Item, Store, Role, User
from schemas.schemas import ItemSchema, StoreSchema, UserSchema, LoginSchema
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from config.config import Config 
app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    try:
        db.engine.connect()
        return "Connection successful"
    except Exception as e:
        return f"Connection failed: {e}"

@app.get("/getAllItems")
def getAllItems():
    items = Item.query.all()
    # Chuyển đổi đối tượng Item thành danh sách các dictionary
    item_Schemas = ItemSchema(many=True)

    return jsonify(item_Schemas.dump(items))


@app.get("/getById/<int:id>")
def getById(id):
    item = Item.query.get(id)
    if item is None:
        return jsonify(
            {
                'message': "not found"
            }
        )
    
    item_schemas = ItemSchema()

    return jsonify(item_schemas.dump(item))

@app.post("/create")
def add_item():
    # Lấy dữ liệu từ yêu cầu HTTP
    json_data = request.get_json()

    # Tạo schema và deserialze dữ liệu
    item_schema = ItemSchema()
    try:
        item_data = item_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Tạo đối tượng Item mới
    new_item = Item(**item_data)

    # Thêm đối tượng vào cơ sở dữ liệu
    db.session.add(new_item)
    db.session.commit()

    # Serialize đối tượng mới và trả về
    result = item_schema.dump(new_item)
    return jsonify(result), 201

@app.delete("/delete/<int:id>")
def deleteOne(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({
        "message": "delete succesfully"
    })

@app.patch("/update/<int:id>")
def updateById(id):
    item = Item.query.get(id)

    item_schema = ItemSchema()
    
    data = item_schema.load(request.get_json())

    try:
        
        # Cập nhật thông tin đối tượng
        item.name = data['name']
        item.price = data['price']
        item.store_id = data['store_id']

        db.session.commit()
        # Serialize đối tượng đã cập nhật và trả về
        result = item_schema.dump(item)
        return jsonify(result), 200
    except ValidationError as err:
        return jsonify({
            "message": f"erorr: {err}"
        }), 404


@app.get("/getAllUser")
def getAllUser():
    data = User.query.all()
    userSchema = UserSchema(many=True)
    return jsonify(userSchema.dump(data))

@app.post("/login")
def login():
    data = request.get_json()
    loginSchema = LoginSchema()
    dataLogin = loginSchema.load(data)
    return jsonify(dataLogin)

@app.post("/register")
def register():
    try:
        data = request.get_json()
        userSchema = UserSchema()
        return jsonify(userSchema.load(data))
    except ValidationError as err:
        return jsonify(err.messages)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
