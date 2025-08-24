ALX Final Project – Inventory Management API
Overview

The Inventory Management API is a RESTful backend system built with Django REST Framework (DRF).
It enables users to add, update, delete, search, and manage inventory items with ease.
This project demonstrates strong backend development skills, API design, and test-driven development.

Features

Add new inventory items
Update item details (price, quantity, etc.)
Delete items from inventory
View all inventory items
Search and filter items by fields
Unit-tested endpoints for reliability

Tech Stack

Programming Language: Python 3.x

Framework: Django, Django REST Framework

Database: SQLite (default, easy swap to PostgreSQL/MySQL)

Version Control: Git & GitHub

Testing: Django’s built-in test framework

Project Structure
ALX_Final_Project/
│── inventory/            # Main app  
│── restaurant_inventory/    # Project settings  
│── manage.py  
│── requirements.txt  
│── README.md  

Setup Instructions

Clone the repository

git clone https://github.com/sissyshobs123/ALX_Final_Project.git
cd ALX_Final_Project


Create and activate a virtual environment

python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run database migrations

python manage.py migrate


Start the development server

python manage.py runserver

Running Tests

Run unit tests to ensure all endpoints work correctly:

python manage.py test

API Endpoints (Sample)
Method	Endpoint	Description
GET	/api/items/	List all items
POST	/api/items/	Create a new item
GET	/api/items/<id>/	Retrieve item details
PUT	/api/items/<id>/	Update an item
DELETE	/api/items/<id>/	Delete an item

Contribution

Contributions are welcome!

Fork the repository

Create a feature branch

Submit a pull request

License

This project is licensed under the MIT License.