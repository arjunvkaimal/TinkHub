# Blogo - Django Blog Application

## Project Overview

Blogo is a simple multi-user blogging platform built with Django. Each registered user can create, edit, and delete their own blog posts, while unauthorized users can only view public posts. The project incorporates user authentication, allowing users to sign up, log in, and manage their posts.

## Features

- User Authentication (Signup, Login, and Logout)
- Password Hashing and Security
- Create, Edit, Delete blog posts (only by the respective authors)
- Public and private blogs
- Responsive and user-friendly UI
- Custom styling with CSS and Bootstrap

## Tech Stack

- Backend: Django 5.1 (Python 3.12)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default)

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/yourusername/Blogo.git
cd Blogo
```

### 2. Set Up the Virtual Environment

```
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```
pip install -r requirements.txt
```

### 4. Migrate the Database

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```
python manage.py createsuperuser
```

This will prompt you to enter a username, email, and password.

### 6. Collect Static Files

To ensure all static files (CSS, JavaScript) are gathered in one place, run:

```
python manage.py collectstatic
```

### 7. Run the Development Server

```
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser.

## User Authentication

- Signup: Users can sign up using the `/signup` page.
- Login: Login via `/login`.
- Logout: Logout via `/logout`.

## Blog Management

- Once logged in, users can create a new blog by visiting `/blog/new/`.
- Users can view their blog posts on the homepage and edit or delete them.
- Only logged-in users can manage their own blogs.
