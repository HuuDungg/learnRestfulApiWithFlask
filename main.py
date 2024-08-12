from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/train06'
db = SQLAlchemy(app)

@app.route('/')
def index():
    try:
        db.engine.connect()
        return "Connection successful"
    except Exception as e:
        return f"Connection failed: {e}"

if __name__ == "__main__":
    app.run(debug=True)
