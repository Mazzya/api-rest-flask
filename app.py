from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(140), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to this simple API developed with Flask!",
        "author": "Mazzya",
        "Github": "https://www.github.com/Mazzya",
        "Github Project": ""
    })

@app.route("/products", methods = ['POST'])
def addProduct():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    new_product = Product(name, description, price, quantity)
    db.session.add(new_product)
    db.session.commit()
    return task_schema.jsonify(new_product)

@app.route("/products")
def getProducts():
    products = Product.query.filter_by().all()
    if products is not None:
        return tasks_schema.jsonify(products)
    return jsonify({"message": "products not found"})

@app.route("/products/<int:id>")
def getProduct(id):
    product = Product.query.get(id)
    if product is not None:
        return task_schema.jsonify(product)
    return jsonify({"message": "product not found"})

@app.route("/products/<int:id>", methods=['PUT'])
def editProduct(id):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    product = Product.query.filter_by(id = id).first()
    if product is not None:
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        db.session.commit()
        return task_schema(product)
    return jsonify({"message": "product not found"})

@app.route("/products/<int:id>", methods = ['DELETE'])
def deleteProduct(id):
    product = Product.query.get(id)
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "product deleted"})
    return jsonify({"message": "product not found"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)