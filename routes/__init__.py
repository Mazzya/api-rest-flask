# Endpoints
from flask import request, render_template, redirect, url_for, jsonify
from app import app, db
from schemas.products import Product, TaskSchema, task_schema, tasks_schema

productNotFoundMessage = "Product not found"

# This function handles 404 error
@app.errorhandler(404)
def pageNotFound(error):
    return jsonify({"message": "page not found 😅"}), 404

# Home page
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to this simple API developed with Flask!",
        "author": "Mazzya",
        "Github": "https://www.github.com/Mazzya",
        "Github Project": ""
    })

# Add new product
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

# Get all products
@app.route("/products")
def getProducts():
    products = Product.query.filter_by().all()
    if products is not None:
        return tasks_schema.jsonify(products)
    return jsonify({"message": "products not found"})

# Get product by id
@app.route("/products/<int:id>")
def getProduct(id):
    product = Product.query.get(id)
    if product is not None:
        return task_schema.jsonify(product)
    return jsonify({"message": productNotFoundMessage})

# Update product
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
    return jsonify({"message": productNotFoundMessage})

# Delete product
@app.route("/products/<int:id>", methods = ['DELETE'])
def deleteProduct(id):
    product = Product.query.get(id)
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "product deleted"})
    return jsonify({"message": productNotFoundMessage})