from flask import Flask, request, jsonify

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

@app.post("/createItem/<string:name>")
def createNew(name):
    requestData = request.get_json()
    newStore = {
        "name": requestData["name"],
        "items": name
    }
    if not newStore:
        return jsonify(f"no data input {name}")
    stores.append(newStore)
    return stores


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)