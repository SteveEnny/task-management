# Task Management API

A RESTful API for managing tasks, built with **Django REST Framework**.
Features include user registration, login (token-based), and full CRUD operations for tasks with authentication, pagination, and user-specific task filtering.

---

## 🔹 Features

1. **User Authentication**

   - Register a new user
   - Login to receive an authentication token
   - Token-based authentication for API requests

2. **Task Management**

   - Create, read, update, and delete tasks
   - Each task belongs to a user
   - Fields: `title`, `description`, `status`, `priority`, `due_date`, `start_date`
   - Pagination for listing tasks
   - Custom response structure:
     ```json
     {
       "result": [...],
       "message": "success",
       "count": 2,
        "next": null,
        "previous": null,
        "results": [...],
     }
     ```

3. **Task Filtering**
   - Users can only see and modify their own tasks

---

## 🔹 Project Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. python manage.py runserver

```bash
python manage.py runserver
```

### 5. python manage.py runserver

```bash
python manage.py runserver
```
