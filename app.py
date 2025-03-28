# app.py
from flask import Flask
from config import Config
from db import db, ma
from routes.users import user_routes
from routes.products import product_routes
from routes.orders import order_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

# Register Blueprints
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(product_routes, url_prefix='/products')
app.register_blueprint(order_routes, url_prefix='/orders')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
