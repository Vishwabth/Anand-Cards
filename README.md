# Anand Cards–E-Commerce Web Application

A full-stack **Django web application** for managing and selling wedding invitation cards.  
Includes **user authentication, product catalog, shopping cart, orders, and admin functionality** with responsive templates and media support.  

---

## 🚀 Features
- **User Authentication**
  - Signup, login, and account management (`Accounts/`).
- **Admin Panel**
  - Manage products, orders, and users (`Admin/`).
- **Product Catalog**
  - Wedding card categories: Hindu, Muslim, Christian, Worship (`Products/`).
- **Shopping Cart**
  - Add, view, and update cart items (`Cart/`).
- **Orders**
  - Checkout, order confirmation, invoice PDF generation (`Orders/`).
- **Media & Static Files**
  - Product images and sample wedding cards (`/media`, `/static`).
- **Responsive Templates**
  - Modular HTML templates for each app (`templates/`).

---

## 📂 Project Structure
```bash
Ac/
│── manage.py
│── Ac/ # Django project settings
│── Accounts/ # User login, signup, account pages
│── Admin/ # Custom admin module
│── Cart/ # Shopping cart logic + templates
│── Home/ # Landing page + views
│── Orders/ # Checkout, confirmation, order PDFs
│── Products/ # Product catalog (Hindu, Muslim, Christian, Worship cards)
│── media/ # Uploaded media (e.g., wedding cards)
│── static/ # Static images, CSS, JS
│── staticfiles_collected/ # Django collected static files
│── templates/ # App-specific templates
│── db.sqlite3
│── .git/ # Git version contro
```
## ⚙️ Setup & Installation

1. **Clone the repository**
```bash
git clone <repo_url>
cd Ac
```
2. **Create & activate virtual environmen**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Apply migrations**
```bash
python manage.py migrate
```
5. **Create superuser**
```bash
python manage.py createsuperuser
```
6. **Run development server**
```bash
python manage.py runserver
```
 ### 📌 Usage
 - **Home Page → http://127.0.0.1:8000/**
 - **Accounts → /login/, /signup/, /account/**
 - **Products → /products/ (Hindu, Muslim, Christian, Worship cards)**
 - **Cart → /cart/**
 - **Checkout → /orders/checkout/**
 - **Admin → /admin/**

 ### 🛠 Tech Stack
  - **Backend: Django (Python)**
  - **Frontend: HTML, CSS, Bootstrap (templates)**
  - **Database: SQLite (default) / PostgreSQL / MySQL**
  - **Media Handling: Django File Storage for uploads**
  - **Static Files: Collected via Django collectstatic**
