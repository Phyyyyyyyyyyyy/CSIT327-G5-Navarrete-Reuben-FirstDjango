# CampusConnect

A small Django web app for a campus community, built for **CSIT327 (Section G5)** as a first Django project. Students can sign up, log in, and see a personal dashboard. Users with the Admin role also get access to a restricted admin panel.

## Features

- **Custom user model** (`accounts.CustomUser`) extending Django's `AbstractUser` with:
  - `role` — `Student` (default) or `Admin`
  - `course` — optional course/program name
- **Sign up** with username, email, first/last name, course and password
- **Log in / log out** using Django's built-in auth views
- **Dashboard** (login required) showing the user's role, course, total member count and last login date
- **Admin panel** page that only users with the `Admin` role can open (others get a 403)
- **Django admin** integration with a "School Profile" section for editing role and course
- **Bootstrap 5** styling, with form fields styled automatically (including red highlighting on invalid fields)

## Tech stack

- Python 3
- Django 6.1.2
- SQLite (default Django database)
- Bootstrap 5.0.2 (loaded from CDN)

## Project structure

```
campusconnect/        Project settings and root URL config
accounts/             Custom user model, sign-up/login forms and views
dashboard/            Dashboard and admin-panel views
templates/
├── base.html         Shared layout with navbar and messages
├── registration/     login.html, signup.html
├── dashboard/        home.html, admin_panel.html
└── partials/         form_fields.html (reusable form rendering)
manage.py
requirements.txt
```

## Getting started

1. **Clone the repo**

   ```bash
   git clone https://github.com/Phyyyyyyyyyyyy/CSIT327-G5-Navarrete-Reuben-FirstDjango.git
   cd CSIT327-G5-Navarrete-Reuben-FirstDjango
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (to use the Django admin)

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**

   ```bash
   python manage.py runserver
   ```

   Then open <http://127.0.0.1:8000/>.

## Pages

| URL                  | Description                                  | Access           |
|----------------------|----------------------------------------------|------------------|
| `/`                  | Dashboard                                    | Logged-in users  |
| `/accounts/signup/`  | Create an account                            | Everyone         |
| `/accounts/login/`   | Log in                                       | Everyone         |
| `/accounts/logout/`  | Log out (POST)                               | Logged-in users  |
| `/admin-panel/`      | Admin-only page                              | Role = Admin     |
| `/admin/`            | Django admin site                            | Staff users      |

## Giving a user the Admin role

New sign-ups are always **Students**. To make someone an Admin:

1. Log in to `/admin/` with your superuser account.
2. Open **Users** and select the user.
3. Under **School Profile**, change **Role** to `Admin` and save.

That user will now see an **Open admin panel** button on their dashboard.

## Notes

- This project is configured for local development only (`DEBUG = True`, hard-coded `SECRET_KEY`). Don't deploy it as-is.

## Author

Reuben Navarrete — CSIT327, Section G5
