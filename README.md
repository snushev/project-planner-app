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

- Registration is available via POST /register/
- No login/auth yet – public endpoints only

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
- [ ] Token authentication
- ✅ Task filtering and search
- [ ] Activity tracking (who updated what and when)
- [ ] Custom endpoints (/tasks/{id}/mark-done/ etc.)
- [ ] Swagger / Redoc API documentation

## 🧪 API Testing

You can test the API using:
-Django’s built-in browsable API interface
-Postman / Insomnia
-cURL

## 🤝 Contributing

If you'd like to suggest improvements or contribute, feel free to open an issue or pull request!

## 📜 License

This project is open-source and licensed under the MIT License.
