# SM-Technology-project
You can paste this in your README.md file:

🚚 Courier Management System — Backend API
Tech Stack: Django, Django REST Framework, JWT, Stripe (test), PostgreSQL

📄 Project Overview
This is a RESTful backend API for a Courier Management System with 3 roles:

Admin: Manages all users, orders, and can assign delivery men.

Delivery Man: Can view and update status of assigned orders.

User: Can register, log in, create orders, make payments, and track delivery status.

🔐 Authentication
JWT-based login and registration

Token generation via /auth/login/

Role-based access control (admin, delivery, user)

📦 Features by Role
🧑‍💼 Admin
View all orders

Assign delivery men to orders

Full access to users and data

🚚 Delivery Man
View only assigned orders

Update delivery status (pending, delivered, complete)

👤 User
Register / Login

Create order

View and track orders

Make Stripe payments (test)

🔗 Live API
perl
Copy
Edit
https://api/v1/
📤 Postman Collection
Download / View: 

(Upload your exported .json file to Google Drive or GitHub and link it here)

🔐 Login Credentials (Test Users)
Role	Username	Password
Admin	admin	pass1234
Delivery Man	rakesh	pass1234
User	john	pass1234

Database ERD
![image](https://github.com/user-attachments/assets/deb167bb-0e20-4b0c-b747-1eb2c8e81ee2)


