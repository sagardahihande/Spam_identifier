﻿Spam Identifier API
This is a Django-based REST API for marking phone numbers as spam and searching users by name or phone number. It includes user authentication, admin panel access, and an API to interact with user data.

Features
User registration with phone number, email, and password.
Mark phone numbers as spam.
Search users by name or phone number.
Admin panel for managing users.


Setup
1. Install Python and Virtual Environment
Install Python (version 3.8 or higher) from python.org.
Create a virtual environment (optional but recommended):

pip install virtualenv
virtualenv venv
venv\Scripts\activate  # Windows

2. Install Dependencies
Install the required dependencies:
pip install django djangorestframework

3. Setup Database and Migrate
Run the migrations:

python manage.py migrate

4. Create a Superuser
To access the admin panel:

python manage.py createsuperuser

5. Run the Server
Start the development server:

python manage.py runserver
http://127.0.0.1:8000/spam/
http://127.0.0.1:8000/register/

Access the admin panel at http://127.0.0.1:8000/admin/ with the superuser credentials.


API Usage
Register User: POST /api/register/
Mark Phone Number as Spam: POST /spam/

View All Users: GET /users/
You can test the API using Postman or curl.

Admin Panel
URL: http://127.0.0.1:8000/admin/
Log in with your superuser credentials to manage users.
This project enables basic spam identification features and allows user management through Django's admin interface.
