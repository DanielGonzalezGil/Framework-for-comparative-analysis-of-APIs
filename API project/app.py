from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database connection for PostgreSQL
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://danielgonzalez:your_password@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Dont need but added to stop console from giving warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize DB
db = SQLAlchemy(app)

# initialize ma
ma = Marshmallow(app)


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# product Schema
class productSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "qty")


# initialize schema
product_schema = productSchema()
products_schema = productSchema(many=True)


# Create a Product
@app.route("/product", methods=["POST"])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
