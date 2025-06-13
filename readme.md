# 📱 Todo – Django

A production-ready authentication system built with Django and HTML, Bootstrap. Users can sign up and log in using only their unique username and password. Designed for web.

---

## 🚀 Features

- 🔐 Username-based authentication
- 🪄 User deletion
- 🌟 User edit profile
- 🧱 Organized, scalable code structure (views, forms, models)

---

## 🖥️ Tech Stack

+ Django (Python Web Framework)
+ SQLite (lightweight dev database)
+ Django Forms (for login, signup, profile edit)
+ HTML5, Bootstrap 5 (frontend)

---

## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Muha-mmed/myapp.git
cd myapp
```
### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

---

## 🧪 API Endpoints (Sample)

| Method | Endpoint             | Auth Required | Description                       |
| ------ | -------------------- | ------------- | --------------------------------- |
| `GET`  | `/`                  | ✅ Yes         | Home view – list all user's todos |
| `POST` | `/`                  | ✅ Yes         | Create a new todo                 |
| `POST` | `/delete/<id>/`      | ✅ Yes         | Delete a todo by ID               |
| `GET`  | `/update/<todo_id>/` | ✅ Yes         | Show update form for a todo       |
| `POST` | `/update/<todo_id>/` | ✅ Yes         | Update a todo title               |
| `GET`  | `/login/`            | ❌ No          | Show login form                   |
| `POST` | `/login/`            | ❌ No          | Authenticate and log in user      |
| `GET`  | `/signup/`           | ❌ No          | Show registration form            |
| `POST` | `/signup/`           | ❌ No          | Register a new user               |
| `POST` | `/logout/`           | ✅ Yes         | Log out the user                  |
| `GET`  | `/edit-profile/`     | ✅ Yes         | Show profile edit form            |
| `POST` | `/edit-profile/`     | ✅ Yes         | Submit profile update             |
| `POST` | `/delete-account/`   | ✅ Yes         | Delete user account               |


## 🧠 Lessons Learned

## 🧠 Lessons Learned

- How to build a custom authentication system in Django
- Handling user registration, login, logout, profile update, and deletion
- Protecting views with login restrictions (`@login_required`)
- Using Django messages for user feedback
- Structuring Django projects for clarity and scalability


---

## 📄 License

MIT License

---

## ✨ Credits

Built with ❤️ by [Muhammed](https://www.linkedin.com/in/muhd8/)