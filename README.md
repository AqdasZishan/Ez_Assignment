---

# File Share Project

This Django project allows users to log in with a username that determines access to different portals. Admin users can upload files to the server, while regular users can view and download these files.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Overview

The File Share Project is designed to facilitate file uploads and downloads using a simple login system. Admin users are granted access to a custom dashboard for file management, while regular users can access a separate dashboard to view and download the uploaded files.

## Features

- **User Authentication**: 
  - Admins can log in with usernames starting with "admin".
  - Users can log in with usernames starting with "user".

- **Admin Portal**: 
  - Admin users can upload files.
  - Uploaded files are stored locally in a designated directory.

- **User Portal**: 
  - Users can view a list of files uploaded by the admin.
  - Users can download the files.

## Technologies Used

- Python
- Django
- HTML/CSS
- SQLite (default database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/file_share_project.git
   cd file_share_project
   ```

2. Install the required packages:

   ```bash
   pip install django
   ```

3. Apply the migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Login**: Enter your username to access the appropriate portal.
  - For Admin: Use a username that starts with "admin".
  - For User: Use a username that starts with "user".

- **Admin Dashboard**: Here, you can upload files. The uploaded files are saved in the `media/uploads/` directory.

- **User Dashboard**: You can view all uploaded files and download them.

## File Structure

```
file_share_project/
├── manage.py
├── file_share_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portal/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
        ├── login.html
        ├── boss_dashboard.html
        └── user_dashboard.html
```
---
