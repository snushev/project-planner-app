# 🗂️ TaskHub API

A simple and extensible **task and project management API**, built with Django REST Framework.  
Users can register, create projects, add tasks with tags, and comment on tasks.

---

## 🚀 Features

- ✅ User registration via API
- ✅ View all registered users
- ✅ Create/read/update/delete:
  - Projects (per user)
  - Tasks (with status & deadline)
  - Tags (many-to-many with tasks)
  - Comments (per task and per user)
- ✅ Pagination enabled (5 items per page)
- ✅ Only authenticated users can create or view their own data
- ✅ Clean RESTful API structure via `ModelViewSet`s
- ✅ Nested serializers for clearer responses (e.g. project owner info)

---

## 🛠 Tech Stack

- Python 3.11+
- Django
- Django REST Framework
- SQLite (for development)

---

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/taskhub-api.git
cd taskhub-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔐 Authentication

🔒 Currently:

The API uses **session-based authentication**.

- ✅ Register via `POST /register/`
- ✅ Login via `POST /login/` (creates a browser session)
- ✅ Logout via `GET /logout/` (destroys the session)
- ✅ DRF’s browsable API works fully with login sessions

No token authentication is required.

🧪 Coming soon:

- Token-based authentication (DRF's TokenAuthentication)
- Login/logout endpoints
- JWT support (optional)

## 🧭 Filtering, Search & Ordering (Planned)

- Filter tasks by status, tags, and deadline
- Search projects and tasks by name
- Ordering support (e.g. by created_at, deadline)

## 📅 Roadmap

- ✅ Basic CRUD for Projects, Tasks, Tags, Comments
- ✅ User registration
- ✅ Pagination (5 per page)
- ✅ Task filtering and search
- ✅ Login/logout via session
- ✅ Swagger / Redoc API documentation
- [ ] Activity tracking (who updated what and when)
- [ ] Custom endpoints (/tasks/{id}/mark-done/ etc.)
- [ ] (Optional) Token or JWT auth as alternative

## 🧪 API Testing

You can test the API using:

- ✅ Django’s built-in browsable API interface (with login session)
- ✅ Postman / Insomnia (optional – not required for auth)
- ✅ cURL

## 🤝 Contributing

If you'd like to suggest improvements or contribute, feel free to open an issue or pull request!

## 📜 License

This project is open-source and licensed under the MIT License.
