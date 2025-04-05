Ready-to-Assemble Furniture API
Welcome to the Ready-to-Assemble Furniture API! This API is designed to manage users, furniture items, orders, reviews, customizations, and much more. Built using Django and Django REST Framework, it is highly scalable and offers robust CRUD functionality, role-based access control, and search/filtering capabilities.

Features
User Management: Register, authenticate, and manage users with roles (admin, seller, or customer).

Furniture Inventory: Manage furniture details, categorized with filtering and search capabilities.

Order Processing: Seamless order handling with status tracking.

Wishlist: Enable users to maintain personalized wishlists.

Product Customizations: Support customers in personalizing furniture.

Promotions: Add and manage discounts for sales.

Reviews: Let users share feedback through product reviews.

Assembly Guides: Provide users with downloadable instructions.

Technologies Used
Backend Framework: Django & Django REST Framework (DRF)

Database: PostgreSQL or SQLite (Development)

API Testing Tool: Postman

Authentication: JWT (JSON Web Tokens)

Installation Instructions
Prerequisites
Install Python 3.11 or higher.

Set up PostgreSQL or your preferred database system.

Install Django and related dependencies.

Steps
Clone the repository:

bash
git clone https://github.com/Eve-code93/ready_to_assemble_furniture_api.git
cd ready_to_assemble_furniture_api
Create a virtual environment:

bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install the required dependencies:

bash
pip install -r requirements.txt
Create a .env file for environment variables:

plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://username:password@localhost:5432/furniture_db
DEBUG=True
Apply migrations:

bash
python manage.py migrate
Start the server:

bash
python manage.py runserver
API Endpoints
Below is a detailed list of API endpoints available in the project:

Authentication
POST /api/auth/login/ Authenticate a user and retrieve a JWT token.

Users
GET /api/users/ List all users (Admin only).

POST /api/users/register/ Register a new user (Open to all).

Furniture
GET /api/furniture/ Retrieve a list of furniture items. Supports filtering by category and price, search by name and description, and ordering by price or name.

POST /api/furniture/ Add a new furniture item (Seller/Admin only).

PUT /api/furniture/<id>/ Update an existing furniture item (Seller/Admin only).

DELETE /api/furniture/<id>/ Delete a furniture item (Seller/Admin only).

Orders
GET /api/orders/ Retrieve orders for the authenticated user.

POST /api/orders/ Place a new order.

Wishlist
GET /api/wishlist/ Retrieve the authenticated user's wishlist.

POST /api/wishlist/ Add an item to the wishlist.

DELETE /api/wishlist/<id>/ Remove an item from the wishlist.

Reviews
GET /api/reviews/ Retrieve all product reviews.

POST /api/reviews/ Add a review for a product (Authenticated users only).

Promotions
GET /api/promotions/ Retrieve active promotions.

POST /api/promotions/ Add a new promotion (Admin only).

PUT /api/promotions/<id>/ Update a promotion (Admin only).

DELETE /api/promotions/<id>/ Remove a promotion (Admin only).

Customizations
GET /api/customizations/ List all customizations for the authenticated user.

POST /api/customizations/ Add a new customization.

Assembly Guides
GET /api/assembly-guides/ Download an assembly guide for a specific furniture item (Authenticated users only).

Testing the API
Use Postman to interact with the API endpoints:

Authenticate to obtain a JWT token:

plaintext
POST /api/auth/login/
Authorization: Bearer <your_jwt_token>
Include the token in the headers for protected routes.

Test filtering, searching, and CRUD operations for resources like Furniture.

Future Enhancements
Add payment gateway integration for orders.

Implement user notifications via email or SMS.

Expand search capabilities using Elasticsearch.

Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new feature branch:

bash
git checkout -b feature/<feature_name>
Commit your changes:

bash
git commit -m "Add new feature"
Push to your forked repository:

bash
git push origin feature/<feature_name>
Submit a pull request.

License
This project is licensed under the MIT License.
