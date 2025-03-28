# routes/products.py
from flask import Blueprint, request, jsonify
from db import db
from models import Product
from schemas import product_schema, products_schema

product_routes = Blueprint('products', __name__)

@product_routes.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(product_name=data['product_name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

@product_routes.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)
