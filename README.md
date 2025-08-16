# ALX Final Project - Inventory Management API

## 📌 Project Overview
This project is an **Inventory Management REST API** built with Django REST Framework.  
It allows users to **add, update, remove, view, and search items** in an inventory system.  
The API is designed to be simple, scalable, and secure, serving as a foundation for a real-world inventory management solution.

---

## 🚀 Features
- Add new items to inventory ✅  
- Update item details (e.g., price, quantity)  
- Remove items from inventory  
- View all items in the inventory  
- Search and filter items by different fields  
- API tested with unit tests for reliability  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Django**  
- **Django REST Framework (DRF)**  
- **SQLite** (default, can be swapped for PostgreSQL/MySQL)  
- **Git & GitHub** for version control  

---

## 📂 Project Structure

ALX_Final_Project/
│── inventory/ # Main app
│── ALX_Final_Project/ # Project settings
│── manage.py
│── requirements.txt
│── README.md

Setup Instruction 
1. Clone the repository:
   ```bash
   git clone https://github.com/sissyshobs123/ALX_Final_Project.git
   cd ALX_Final_Project
2. Create & activate a virtual environment:   
   python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install dependencies:
pip install -r requirements.txt
4. Run migrations:
python manage.py migrate
5. Start the server:
python manage.py runserver