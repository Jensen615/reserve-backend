from db import db
import json

from flask import Flask
from flask import request

app = Flask(__name__)
db_filename = "reserve.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(data, code=404):
    return json.dumps({"error": data}), code





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)