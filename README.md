Blog Backend Project

This project implements a backend system for a blog using Django, designed to manage blog posts, user authentication, and profiles.

Features

User Management:

Authentication (registration, login, logout)
Custom user model with extended fields (name, surname)

Blog Management:

CRUD operations for blog posts
Commenting system with likes and dislikes
Categorization and tagging of posts

Profile Management:

User profiles with optional profile image and bio
Integration with Django admin for profile viewing and limited editing

API Endpoints:

RESTful APIs for blog posts, comments, user profiles
Authentication and authorization using JWT tokens


Technologies Used:

Django: Backend framework
Django REST Framework: API development
PostgreSQL: Database
React: Frontend framework (not covered in this README)
Setup Instructions:

1.Clone the repository:

git clone https://github.com/MehranBabayev/blog_task.git
cd blog_task

2.Set up virtual environment:

python3 -m venv .venv
source .venv/bin/activate

3.Install dependencies:

pip install -r requirements.txt

4.Apply database migrations:

python manage.py migrate

5.Create a superuser:

python manage.py createsuperuser

6.Run the development server:

python manage.py runserver
