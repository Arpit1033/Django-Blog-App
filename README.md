# Django Blog Application

A fully featured, responsive Blog Application built with Django 5.0. It allows users to create, read, update, and delete blog posts, along with full user authentication, profile management, and password reset capabilities.

## ✨ Features

- **User Authentication:** 
  - Register, Login, and Logout functionality.
  - Password Reset via Email (with secure tokens).
- **User Profiles:** 
  - Dedicated user profiles with custom profile picture uploads.
- **Blog Posts (CRUD):** 
  - Create new posts, view detailed posts, update existing posts, and delete posts.
  - Authorization checks ensure only the author can update or delete their posts.
- **Pagination & Filtering:** 
  - Posts are paginated on the home page.
  - View all posts written by a specific user.
- **UI & Forms:** 
  - Beautifully styled forms using `django-crispy-forms` with Bootstrap 4.

## 🛠️ Tech Stack
- **Backend Framework:** Django 5.0.1
- **Database:** SQLite3 (Default for development)
- **Styling:** Custom CSS + Bootstrap 4 (via crispy-bootstrap4)
- **Image Processing:** Pillow 10.2.0

## 🚀 Local Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Django-Blog-App.git
cd Django-Blog-App
```

### 2. Set up a Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
If you want to test the **password reset** functionality, set up environment variables for your email address. 
```bash
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-app-password"
```

### 5. Run Database Migrations
Navigate into the `django_project` directory and run migrations:
```bash
cd django_project
python manage.py migrate
```

### 6. Create a Superuser (Optional)
To access the Django admin panel (`/admin/`):
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.