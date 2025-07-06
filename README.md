🚚 Courier Management System — Backend API
Tech Stack: Django · Django REST Framework · JWT · Stripe (Test Mode) · PostgreSQL

📄 Project Overview
This is a RESTful backend API for a Courier Management System designed to handle real-world courier operations with role-based access.

Supported Roles:
Admin: Full access to manage users, orders, and assign delivery men.

Delivery Man: Can view and update the status of assigned orders.

User: Can register, log in, create orders, make payments, and track delivery status (pending, delivered, complete).

🔐 Authentication
JWT-based registration and login

Role-based permissions using is_admin, is_delivery, and is_user flags

Tokens are issued via: POST /api/v1/auth/login/

📦 Features by Role
🧑‍💼 Admin
View all orders

Assign delivery men to orders

View/manage all users

🚚 Delivery Man
View only assigned orders

Update order delivery status

👤 User
Register / Login

Create new orders

Track order status

Make payments via Stripe (test mode only)

🔗 Live API
🌐 Base URL:
https://sm-technology-project.onrender.com/api/v1/

📤 Postman Collection
🧪 Click here to view/download Postman collection
(Upload your Postman .json to GitHub or Google Drive and replace the link)

🔐 Test Login Credentials
Role	Username	Password
Admin	admin	pass1234
Delivery Man	rakesh	pass1234
User	john	pass1234

🗃️ ERD (Entity Relationship Diagram)

Or embed the image from a site like dbdiagram.io or drawsql.app

✅ Example API Endpoints
Method	Endpoint	Description
POST	/auth/register/	User registration
POST	/auth/login/	User login (returns JWT token)
GET	/orders/	View orders (by role access)
POST	/orders/	Create order (user only)
PATCH	/orders/:id/assign/	Assign delivery man (admin only)
PATCH	/orders/:id/status/	Update delivery status (delivery only)
POST	/orders/:id/pay/	Make payment using Stripe (user only)


📦 Setup Instructions
# Clone the repo
git clone https://github.com/rakeshyadav9698/SM-Technology-project.git
cd SM-Technology-project

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
