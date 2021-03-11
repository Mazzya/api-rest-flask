from app import db, ma

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

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)