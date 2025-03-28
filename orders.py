# routes/orders.py
 from flask import Blueprint, request, jsonify
 from db import db
 from models import Order, OrderProduct
 from schemas import order_schema, orders_schema
 
 order_routes = Blueprint('orders', __name__)
 
 @order_routes.route('/', methods=['POST'])
 def create_order():
     data = request.get_json()
     new_order = Order(user_id=data['user_id'])
     db.session.add(new_order)
     db.session.commit()
     return order_schema.jsonify(new_order)
 
 @order_routes.route('/<order_id>/add_product/<product_id>', methods=['PUT'])
 def add_product_to_order(order_id, product_id):
     order_product = OrderProduct(order_id=order_id, product_id=product_id)
     db.session.add(order_product)
     db.session.commit()
     return jsonify({'message': 'Product added to order'})
 
 @order_routes.route('/<order_id>/remove_product/<product_id>', methods=['DELETE'])
 def remove_product_from_order(order_id, product_id):
     order_product = OrderProduct.query.filter_by(order_id=order_id, product_id=product_id).first()
     if order_product:
         db.session.delete(order_product)
         db.session.commit()
     return jsonify({'message': 'Product removed from order'})
 
 @order_routes.route('/user/<user_id>', methods=['GET'])
 def get_orders_for_user(user_id):
     orders = Order.query.filter_by(user_id=user_id).all()
     return orders_schema.jsonify(orders)
