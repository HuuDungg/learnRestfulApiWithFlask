from flask import Flask, request, jsonify
from schemas import ItemSchema
from marshmallow import ValidationError
app = Flask(__name__)

stores = [
    {
        "name": "Huu Dung Tran",
        "items": [
            {
                "name": "bread",
                "price": 342
            },
            {
                "name": "juice",
                "price": 6456
            },
            {
                "name": "saucess",
                "price": 765
            },
            {
                "name": "cream",
                "price": 765
            }
        ]
    }
]

@app.get("/getItems")
def getMyItems():
    return jsonify(stores)

@app.post("/createItem")
def createNew():
    try:
        requestData = request.get_json()
        itemsch = ItemSchema()
        data = itemsch.load(requestData)
        stores.append(data)
        return stores
    except ValidationError as err:
        return jsonify(err.messages)

@app.delete("/delete/<int:id>")
def deleteUnit(id):
    check = stores.remove(stores[id])
    if check:
        return jsonify("remove successfuly")
    else:
        return jsonify("some thing went wrong")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)