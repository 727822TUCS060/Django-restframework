# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.

# Django REST Framework, ORM and React CRUD Project

A full-stack learning project demonstrating **Django, Django REST Framework (DRF), MySQL, Django ORM, JWT Authentication, Postman API testing, React, Axios, and CORS**.

The repository contains examples of REST API development, database relationships, ORM queries, CRUD operations, authentication, and connecting a React frontend with a Django REST backend.

---

# Features

- Django project setup
- Django REST Framework APIs
- MySQL database integration
- Django ORM queries
- ORM filter queries
- ForeignKey relationships
- One-to-One relationships
- Many-to-One relationships
- Serializers
- Class-Based CRUD operations
- APIView
- ModelViewSet
- JWT authentication and authorization
- Access and refresh tokens
- Postman API testing
- React CRUD operations
- Axios API connectivity
- CORS configuration
- Backend and frontend integration

---

# Technology Stack

## Backend

- Python
- Django
- Django REST Framework
- MySQL
- mysqlclient

## Authentication

- djangorestframework-simplejwt
- JWT (JSON Web Token)

## Frontend

- React
- Axios

## API Testing

- Postman

---

# Project Structure

A typical repository structure can be:

```text
django-project/
│
├── django-restframework/
│   ├── manage.py
│   ├── project/
│   └── api/
│
├── orm/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
│
├── react-frontend/
│   ├── src/
│   ├── package.json
│   └── ...
│
├── postman/
│   └── API collection files
│
├── requirements.txt
└── README.md
```

The exact folder names may differ depending on the repository structure.

---

# Prerequisites

Before setting up the project, install:

- Python 3.x
- MySQL Server
- MySQL Workbench (recommended)
- Node.js and npm
- Git
- Postman
- VS Code or another code editor

Check Python:

```bash
python --version
```

Check pip:

```bash
pip --version
```

Check Node.js:

```bash
node --version
```

Check npm:

```bash
npm --version
```

---

# Backend Setup

## 1. Clone the Repository

Clone the GitHub repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the repository:

```bash
cd YOUR-REPOSITORY
```

If your Django project is inside a specific folder:

```bash
cd django-restframework
```

---

# 2. Create a Virtual Environment

Creating a virtual environment keeps the project's Python dependencies separate from the system Python installation.

## Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

For PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## macOS/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

After activation, the terminal should show:

```text
(venv)
```

---

# 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 4. Install Django

Install Django:

```bash
pip install django
```

Check the Django version:

```bash
django-admin --version
```

---

# 5. Install Django REST Framework

Install Django REST Framework:

```bash
pip install djangorestframework
```

DRF is used to build REST APIs and provides serializers, API views, generic views, viewsets, routers, authentication support, and other API development features.

---

# 6. Install Simple JWT

Install Simple JWT:

```bash
pip install djangorestframework-simplejwt
```

Simple JWT is used to implement JWT-based authentication and authorization.

It provides:

- Access tokens
- Refresh tokens
- JWT authentication
- Token refresh functionality

---

# 7. Install MySQL Client

Install the MySQL database connector:

```bash
pip install mysqlclient
```

This allows Django to communicate with MySQL.

If `mysqlclient` installation fails on Windows, make sure the required MySQL/MariaDB development dependencies or a compatible wheel are available for your Python version.

---

# 8. Install CORS Headers

Install:

```bash
pip install django-cors-headers
```

This package allows the React frontend and Django backend to communicate when they are running on different origins/ports.

For example:

```text
React:
http://localhost:5173

Django:
http://127.0.0.1:8000
```

Without appropriate CORS configuration, the browser can block API requests between these origins.

---

# 9. Install All Libraries Together

The main backend packages can be installed using:

```bash
pip install django djangorestframework djangorestframework-simplejwt mysqlclient django-cors-headers
```

Or create a `requirements.txt` file:

```text
Django
djangorestframework
djangorestframework-simplejwt
mysqlclient
django-cors-headers
```

Then install:

```bash
pip install -r requirements.txt
```

---

# MySQL Database Setup

## 10. Start MySQL

Make sure MySQL Server is running.

You can use:

- MySQL Workbench
- MySQL Command Line
- XAMPP
- WAMP
- Another MySQL server installation

---

# 11. Create a Database

Open MySQL Workbench or MySQL command line.

Create a database:

```sql
CREATE DATABASE drf_db;
```

You can choose another database name, but the same name must be used in Django's `settings.py`.

Check the database:

```sql
SHOW DATABASES;
```

---

# 12. Configure Django Database

Open:

```text
settings.py
```

Find:

```python
DATABASES
```

Configure MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drf_db',
        'USER': 'root',
        'PASSWORD': 'YOUR_MYSQL_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your local MySQL password.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drf_db',
        'USER': 'root',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Database configuration

| Setting | Example |
|---|---|
| ENGINE | `django.db.backends.mysql` |
| NAME | `drf_db` |
| USER | `root` |
| PASSWORD | Your MySQL password |
| HOST | `localhost` |
| PORT | `3306` |

Do not commit your actual database password to a public GitHub repository.

For production, use environment variables.

---

# Django Settings Configuration

## 13. Add Django REST Framework

Open `settings.py`.

Add:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

If your API app is called `api`, also add:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

Use the actual app name from your project.

---

# 14. Add CORS Headers

Add:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]
```

---

# 15. Add CORS Middleware

Add `CorsMiddleware` near the beginning of the middleware list:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

It is recommended to place `CorsMiddleware` before `CommonMiddleware`.

---

# CORS Configuration

## 16. Allow React Frontend

For local development, if React runs on:

```text
http://localhost:5173
```

configure:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
```

If your React development server uses:

```text
http://127.0.0.1:5173
```

you can add:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

---

# CORS Allow All Option

For simple local development, you can use:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

However, this should generally not be used for a production application.

For production, specify only trusted frontend origins:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
```

---

# Django REST Framework Configuration

## 17. Configure DRF

Add:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

This tells Django REST Framework to use JWT authentication for protected APIs.

---

# JWT Authentication Setup

## 18. Add JWT URLs

In your main `urls.py`:

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

# JWT Login Flow

The authentication flow is:

```text
React/Postman
      |
      v
Username + Password
      |
      v
/api/token/
      |
      v
Django Authentication
      |
      v
Access Token + Refresh Token
      |
      v
Use Access Token
      |
      v
Protected API
```

---

# Get JWT Token Using Postman

## Request

Method:

```text
POST
```

URL:

```text
http://127.0.0.1:8000/api/token/
```

Body:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Select:

```text
Body
→ raw
→ JSON
```

A successful response will contain tokens similar to:

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

---

# Use JWT Access Token

For a protected API, add the Authorization header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

In Postman:

```text
Authorization
→ Type: Bearer Token
→ Token: YOUR_ACCESS_TOKEN
```

---

# Refresh JWT Token

When the access token expires, use the refresh token.

Method:

```text
POST
```

URL:

```text
http://127.0.0.1:8000/api/token/refresh/
```

Body:

```json
{
    "refresh": "YOUR_REFRESH_TOKEN"
}
```

The API will return a new access token.

---

# Database Migrations

After configuring MySQL:

## Create migrations

```bash
python manage.py makemigrations
```

## Apply migrations

```bash
python manage.py migrate
```

---

# Create Superuser

Create a Django admin user:

```bash
python manage.py createsuperuser
```

Enter:

```text
Username:
Email:
Password:
```

Then run:

```bash
python manage.py runserver
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# Run Django Server

```bash
python manage.py runserver
```

Default URL:

```text
http://127.0.0.1:8000/
```

---

# Django ORM

This repository demonstrates different Django ORM operations.

## Create

```python
Student.objects.create(
    name="Kishore",
    age=23
)
```

## Get

```python
Student.objects.get(id=1)
```

## Get by condition

```python
Student.objects.get(
    name="Kishore",
    age=23
)
```

## Get all records

```python
Student.objects.all()
```

## Filter

```python
Student.objects.filter(
    age=23
)
```

## Multiple filters

```python
Student.objects.filter(
    age=23,
    grade="12th"
)
```

## Exclude

```python
Student.objects.exclude(
    age=23
)
```

## Order By

Ascending:

```python
Student.objects.all().order_by('name')
```

Descending:

```python
Student.objects.all().order_by('-name')
```

## First

```python
Student.objects.first()
```

## Last

```python
Student.objects.last()
```

## Count

```python
Student.objects.count()
```

---

# ORM Filter Queries

Examples:

## Greater Than

```python
Student.objects.filter(age__gt=18)
```

## Greater Than or Equal

```python
Student.objects.filter(age__gte=18)
```

## Less Than

```python
Student.objects.filter(age__lt=18)
```

## Less Than or Equal

```python
Student.objects.filter(age__lte=18)
```

## Contains

```python
Student.objects.filter(name__contains="ki")
```

## Case-Insensitive Contains

```python
Student.objects.filter(name__icontains="ki")
```

## Starts With

```python
Student.objects.filter(name__startswith="K")
```

## Ends With

```python
Student.objects.filter(name__endswith="e")
```

## Range

```python
Student.objects.filter(age__range=(18, 25))
```

## Is Null

```python
Student.objects.filter(age__isnull=True)
```

---

# ForeignKey Relationship

A ForeignKey creates a Many-to-One relationship.

Example:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
```

One author can have multiple books.

Relationship:

```text
Author
  |
  +---- Book
  |
  +---- Book
  |
  +---- Book
```

---

# ForeignKey Query

Get an author:

```python
author = Author.objects.get(id=1)
```

Get books belonging to that author:

```python
books = author.books.all()
```

Using the related name:

```python
Author.objects.get(id=1).books.all()
```

---

# Many-to-One Relationship

A ForeignKey represents a Many-to-One relationship.

Example:

```text
Many Books
     |
     v
 One Author
```

Multiple books can belong to one author.

---

# One-to-One Relationship

Example:

```python
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
```

Relationship:

```text
One User
   |
   v
One Profile
```

A user can have one profile.

---

# Many-to-Many Relationship

Example:

```python
class Student(models.Model):
    courses = models.ManyToManyField(Course)
```

Relationship:

```text
Student <----> Course
```

A student can have multiple courses and a course can have multiple students.

---

# Serializers

Django REST Framework serializers convert Django model instances into JSON data and validate incoming API data.

Example:

```python
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
```

---

# CRUD Operations

CRUD means:

```text
C = Create
R = Read
U = Update
D = Delete
```

The API demonstrates CRUD operations using Django REST Framework.

## Create

```text
POST
```

## Read

```text
GET
```

## Update

```text
PUT
PATCH
```

## Delete

```text
DELETE
```

---

# Class-Based CRUD Operations

Django REST Framework can implement CRUD operations using class-based views.

Example:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentAPI(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
```

The exact implementation depends on the project's models and serializers.

---

# ModelViewSet

The repository also demonstrates CRUD operations using `ModelViewSet`.

Example:

```python
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

A `ModelViewSet` provides common CRUD actions:

```text
list
retrieve
create
update
partial_update
destroy
```

---

# Router Configuration

Example:

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()

router.register(
    'students',
    StudentViewSet,
    basename='students'
)

urlpatterns = router.urls
```

This can create API routes such as:

```text
GET     /students/
POST    /students/
GET     /students/1/
PUT     /students/1/
PATCH   /students/1/
DELETE  /students/1/
```

---

# Postman API Testing

Postman is used to test the Django REST APIs before connecting the React frontend.

Typical operations:

```text
GET
POST
PUT
PATCH
DELETE
```

---

# Example GET Request

```text
GET
http://127.0.0.1:8000/api/students/
```

This retrieves the student records.

---

# Example POST Request

```text
POST
http://127.0.0.1:8000/api/students/
```

JSON:

```json
{
    "name": "Kishore",
    "age": 23,
    "grade": "12th"
}
```

---

# Example PUT Request

```text
PUT
http://127.0.0.1:8000/api/students/1/
```

JSON:

```json
{
    "name": "Kishore Updated",
    "age": 24,
    "grade": "College"
}
```

---

# Example DELETE Request

```text
DELETE
http://127.0.0.1:8000/api/students/1/
```

---

# Protected API Testing

For JWT-protected APIs:

Postman:

```text
Authorization
    |
    +-- Type: Bearer Token
    |
    +-- Token: YOUR_ACCESS_TOKEN
```

The request will be sent with:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

# React Frontend Setup

The repository also demonstrates connecting React with the Django REST API.

Make sure Node.js is installed.

Check:

```bash
node --version
```

Check npm:

```bash
npm --version
```

Move into the React folder:

```bash
cd react-frontend
```

Install dependencies:

```bash
npm install
```

Install Axios:

```bash
npm install axios
```

---

# Axios API Connection

Example GET request:

```javascript
import axios from "axios";

axios.get("http://127.0.0.1:8000/api/students/")
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.log(error);
    });
```

---

# Axios POST Request

Example:

```javascript
axios.post(
    "http://127.0.0.1:8000/api/students/",
    {
        name: "Kishore",
        age: 23,
        grade: "12th"
    }
)
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.log(error);
});
```

---

# Axios PUT Request

```javascript
axios.put(
    "http://127.0.0.1:8000/api/students/1/",
    {
        name: "Kishore Updated",
        age: 24,
        grade: "College"
    }
)
.then(response => {
    console.log(response.data);
});
```

---

# Axios DELETE Request

```javascript
axios.delete(
    "http://127.0.0.1:8000/api/students/1/"
)
.then(response => {
    console.log(response.data);
});
```

---

# Axios with JWT

For protected APIs, send the access token:

```javascript
axios.get(
    "http://127.0.0.1:8000/api/students/",
    {
        headers: {
            Authorization: `Bearer ${accessToken}`
        }
    }
)
.then(response => {
    console.log(response.data);
});
```

---

# React CRUD Flow

The frontend CRUD flow is:

```text
React Component
      |
      v
Axios
      |
      v
Django REST API
      |
      v
Serializer
      |
      v
Django ORM
      |
      v
MySQL
```

Response:

```text
MySQL
   |
   v
Django ORM
   |
   v
Serializer
   |
   v
Django REST API
   |
   v
Axios
   |
   v
React UI
```

---

# Running Backend and Frontend

Two terminals can be used.

## Terminal 1 - Django

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Go to the Django project:

```bash
cd django-restframework
```

Run:

```bash
python manage.py runserver
```

Backend:

```text
http://127.0.0.1:8000/
```

## Terminal 2 - React

Go to React:

```bash
cd react-frontend
```

Install packages if required:

```bash
npm install
```

Start React:

```bash
npm run dev
```

Typical Vite URL:

```text
http://localhost:5173/
```

---

# CORS Communication

The local development setup typically uses:

```text
React:
http://localhost:5173

        |
        | Axios
        v

Django:
http://127.0.0.1:8000

        |
        v

MySQL
```

The Django backend must allow the React frontend origin.

Example:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

For simple development only:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

For production, avoid allowing every origin and specify trusted domains.

---

# Complete Backend Installation

The complete backend setup can be summarized as:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

cd YOUR-REPOSITORY

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install django

pip install djangorestframework

pip install djangorestframework-simplejwt

pip install mysqlclient

pip install django-cors-headers

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

---

# Complete React Installation

```bash
cd react-frontend

npm install

npm install axios

npm run dev
```

---

# Troubleshooting

## Django Not Installed

Error:

```text
ModuleNotFoundError: No module named 'django'
```

Solution:

```bash
venv\Scripts\activate
pip install django
```

---

## DRF Not Installed

Error:

```text
ModuleNotFoundError: No module named 'rest_framework'
```

Solution:

```bash
pip install djangorestframework
```

---

## Simple JWT Not Installed

Error:

```text
ModuleNotFoundError: No module named 'rest_framework_simplejwt'
```

Solution:

```bash
pip install djangorestframework-simplejwt
```

---

## CORS Error

If the browser displays a CORS error:

1. Make sure `django-cors-headers` is installed.
2. Add `corsheaders` to `INSTALLED_APPS`.
3. Add `CorsMiddleware` to `MIDDLEWARE`.
4. Add the React URL to `CORS_ALLOWED_ORIGINS`.
5. Restart Django.

Example:

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
]
```

Middleware:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

CORS:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
```

Restart:

```bash
python manage.py runserver
```

---

## MySQL Connection Error

Check:

```python
'NAME': 'drf_db',
'USER': 'root',
'PASSWORD': 'YOUR_MYSQL_PASSWORD',
'HOST': 'localhost',
'PORT': '3306',
```

Make sure MySQL is running.

---

## Table Does Not Exist

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## JWT Authentication Failed

Check that:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

is configured.

Also verify the request contains:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

# Security Notes

Do not commit the following to a public GitHub repository:

- MySQL passwords
- Django SECRET_KEY
- JWT secrets
- API keys
- Production credentials

Use environment variables for production configuration.

Do not use:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

in a production application unless you specifically understand the security implications.

For production, configure:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
```

Also set:

```python
DEBUG = False
```

and configure `ALLOWED_HOSTS`.

---

# Learning Topics Covered

This repository covers:

## Django

- Project setup
- Apps
- Models
- Views
- URLs
- Migrations
- Authentication

## Django ORM

- `objects.all()`
- `objects.get()`
- `objects.filter()`
- `objects.exclude()`
- `order_by()`
- `first()`
- `last()`
- `count()`
- Lookup queries
- Relationship queries

## Database Relationships

- ForeignKey
- Many-to-One
- One-to-One
- Many-to-Many

## Django REST Framework

- Serializers
- APIView
- Class-Based Views
- CRUD operations
- ModelViewSet
- Routers
- JSON APIs

## Authentication

- JWT
- Access Token
- Refresh Token
- Bearer Authentication
- Protected APIs

## API Testing

- Postman
- GET
- POST
- PUT
- PATCH
- DELETE
- Authorization headers

## React Integration

- React CRUD
- Axios
- GET requests
- POST requests
- PUT requests
- DELETE requests
- JWT headers
- CORS
- Django API integration

---

# API Development Flow

```text
                  React Frontend
                        |
                        | Axios
                        v
                 Django REST API
                        |
                        v
                  Authentication
                        |
                 +------+------+
                 |             |
              JWT Valid     JWT Invalid
                 |             |
                 v             v
             Serializer      401 Error
                 |
                 v
              ORM Query
                 |
                 v
               MySQL
```

---

# Future Improvements

Possible future improvements include:

- React authentication pages
- JWT token storage and refresh handling
- Protected React routes
- React Router
- Axios interceptors
- Search and filtering
- Pagination
- API documentation using Swagger/OpenAPI
- Docker setup
- Environment variable configuration
- Production deployment
- Role-based authorization
- Advanced Django permissions
- Automated testing
- Unit tests
- API tests
- CI/CD

---

# Author

Kishore

Technologies:

Python | Django | Django REST Framework | MySQL | JWT | React | Axios | Postman

---

# License

This project is created for learning, practice, portfolio, and educational purposes.

Add an appropriate open-source license before distributing the project publicly.
