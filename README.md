# Ready-to-Assemble Furniture API

Welcome to the Ready-to-Assemble Furniture API!  
This API is designed to manage users, furniture items, orders, reviews, customizations, and much more.  
Built using **Django** and **Django REST Framework (DRF)**, it is highly scalable and offers robust CRUD functionality, role-based access control, and search/filtering capabilities.

---

## 🌍 Live Deployment  
The API is live and accessible here:  
👉 [https://evecoder93.pythonanywhere.com/swagger/](https://evecoder93.pythonanywhere.com/)  

---

## 🚀 Features
- **User Management**: Register, authenticate, and manage users with roles (admin, seller, or customer).
- **Furniture Inventory**: Manage furniture details, categorized with filtering and search capabilities.
- **Order Processing**: Seamless order handling with status tracking.
- **Wishlist**: Enable users to maintain personalized wishlists.
- **Product Customizations**: Support customers in personalizing furniture.
- **Promotions**: Add and manage discounts for sales.
- **Reviews**: Let users share feedback through product reviews.
- **Assembly Guides**: Provide users with downloadable instructions.

---

## 🛠 Technologies Used
- **Backend Framework**: Django & Django REST Framework (DRF)  
- **Database**: PostgreSQL or SQLite (Development)  
- **API Testing Tool**: Postman  
- **Authentication**: JWT (JSON Web Tokens)  

---

## ⚙️ Installation Instructions

### Prerequisites
- Python 3.11 or higher
- PostgreSQL (or SQLite for development)
- Django and dependencies installed

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/Eve-code93/ready_to_assemble_furniture_api.git
   cd ready_to_assemble_furniture_api


Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies
pip install -r requirements.txt

Create a .env file
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://username:password@localhost:5432/furniture_db
DEBUG=True

Run migrations
python manage.py migrate


Start the server
python manage.py runserver

API Endpoints

Authentication

POST /api/auth/login/ – Authenticate a user and retrieve a JWT token

Users

GET /api/users/ – List all users (Admin only)

POST /api/users/register/ – Register a new user

Furniture

GET /api/furniture/ – Retrieve a list of furniture items (filter/search/order supported)

POST /api/furniture/ – Add a new furniture item (Seller/Admin only)

PUT /api/furniture/<id>/ – Update furniture (Seller/Admin only)

DELETE /api/furniture/<id>/ – Delete furniture (Seller/Admin only)

Orders

GET /api/orders/ – Retrieve orders for the authenticated user

POST /api/orders/ – Place a new order

Wishlist

GET /api/wishlist/ – Get user’s wishlist

POST /api/wishlist/ – Add item to wishlist

DELETE /api/wishlist/<id>/ – Remove item

Reviews

GET /api/reviews/ – Get all reviews

POST /api/reviews/ – Add review (Authenticated users)

Promotions

GET /api/promotions/ – Get active promotions

POST /api/promotions/ – Add promotion (Admin only)

PUT /api/promotions/<id>/ – Update promotion (Admin only)

DELETE /api/promotions/<id>/ – Delete promotion (Admin only)

Customizations

GET /api/customizations/ – List all customizations for user

POST /api/customizations/ – Add customization

Assembly Guides

GET /api/assembly-guides/ – Download assembly guide (Authenticated users only)


Testing the API

Use Postman to test endpoints.
Example (Authentication):
POST /api/auth/login/
Authorization: Bearer <your_jwt_token>


Future Enhancements
Payment gateway integration
Email/SMS notifications
Advanced search (Elasticsearch)

Contributing
Fork the repository
Create a branch
git checkout -b feature/<feature_name>
Commit changes
git commit -m "Add new feature
Push and submit a PR

📜 License
This project is licensed under the MIT License.