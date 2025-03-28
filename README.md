# Mod3E-CommFlaskAPI

This is a RESTful API for managing an e-commerce platform, built using Flask, SQLAlchemy, and Marshmallow with MySQL as the database. The API supports user management, product catalog management, and order processing with proper relationships.

Features User Management: Create, retrieve, update, and delete users.

Product Management: Manage product catalog with CRUD operations.

Order Processing: Users can place orders and associate products with orders.

Data Validation & Serialization: Utilizes Marshmallow for efficient data handling. Tech Stack Backend: Flask

Database: MySQL

ORM: SQLAlchemy

Validation: Marshmallow

Project Structure app.py – Main entry point of the API.

config.py – Configuration file for database settings.

models.py – Defines the database models.

schemas.py – Handles data serialization and validation.

routes/ – Contains separate route files for users, products, and orders.

requirements.txt – List of dependencies.

Setup & Installation Clone the repository:

bash Copy Edit git clone https://github.com/your-username/ecommerce-api.git cd ecommerce-api Create a virtual environment:

bash Copy Edit python -m venv venv
source venv/bin/activate

Mac/Linux
venv\Scripts\activate

Windows
Install dependencies:

bash Copy Edit pip install -r requirements.txt
Configure database in config.py.

Initialize the database:

bash

Copy Edit python
from app import db
db.create_all()
exit()
Run the application:

bash

python app.py
API Endpoints User Endpoints GET /users – Retrieve all users

POST /users – Create a new user

GET /users/ – Get user by ID

PUT /users/ – Update user by ID

DELETE /users/ – Delete user by ID

Product Endpoints GET /products – Retrieve all products

POST /products – Create a new product

GET /products/ – Get product by ID

PUT /products/ – Update product by ID

DELETE /products/ – Delete product by ID

Order Endpoints POST /orders – Create a new order

PUT /orders/<order_id>/add_product/<product_id> – Add product to order

DELETE /orders/<order_id>/remove_product/<product_id> – Remove product from order

GET /orders/user/<user_id> – Get orders for a user

GET /orders/<order_id>/products – Get all products in an order

Testing Use Postman or cURL to test API endpoints.

Verify stored data using MySQL Workbench.

License This project is open-source and available under the MIT License.
