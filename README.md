# 🎓 Student Management System API (FastAPI + PostgreSQL)

A modern, scalable **REST API** for managing students, courses, and enrollments using **FastAPI, SQLAlchemy, and PostgreSQL**. Built with clean architecture and deployed for real-world usage.

---

## 🚀 Live Demo

🔗 **API Base URL**
[Student Management System API](https://student-management-system-fastapi-smcv.onrender.com?utm_source=chatgpt.com)

📄 **Swagger API Docs**
[API Documentation (Swagger UI)](https://student-management-system-fastapi-smcv.onrender.com/docs?utm_source=chatgpt.com)

> ⚠️ Hosted on Render free tier — first request may take a few seconds to wake up.

---

## 📌 GitHub Repository

🔗 Source Code:
[GitHub Repository](https://github.com/PavanSurisetti/student-management-system-fastapi?utm_source=chatgpt.com)

---

## 🛠 Tech Stack

* ⚡ FastAPI – High-performance backend framework
* 🐘 PostgreSQL – Relational database
* 🧠 SQLAlchemy – ORM for database interaction
* 🔐 Pydantic – Data validation & serialization
* 🌍 Uvicorn – ASGI server
* 🧪 python-dotenv – Environment variable management

---

## ✨ Features

* 👨‍🎓 Create and manage students
* 📚 Create and manage courses
* 🔗 Enroll students into courses
* 📖 Fetch all students
* 📘 Get courses of a specific student
* 👥 Get all students enrolled in a course
* ⚡ Clean RESTful API design
* 🧱 Modular and scalable project structure

---

## 📂 Project Structure

```
student-management-system-fastapi/
├── main.py            # FastAPI routes & business logic
├── models.py          # Database models (Student, Course, Enrollment)
├── database.py        # Database connection & session setup
├── requirements.txt   # Project dependencies
├── .env               # Environment variables (not included in repo)
└── .gitignore         # Ignored files
```

---

## ⚡ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/student-management-system-fastapi.git
```

### 2️⃣ Move into project folder

```bash
cd student-management-system-fastapi
```

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Setup environment variables

Create a `.env` file:

```env
db_url=postgresql+psycopg2://user:password@localhost:5432/StudentManagementSystem
```

### 6️⃣ Run the application

```bash
uvicorn main:app --reload
```

### 7️⃣ Open API docs

[Local Swagger UI](http://127.0.0.1:8000/docs?utm_source=chatgpt.com)

---

## 🔗 API Endpoints

| Method | Endpoint                 | Description              |
| ------ | ------------------------ | ------------------------ |
| GET    | `/`                      | Welcome message          |
| POST   | `/students`              | Create a student         |
| GET    | `/students`              | Get all students         |
| POST   | `/courses`               | Create a course          |
| POST   | `/enroll`                | Enroll student in course |
| GET    | `/students/{id}/courses` | Get student’s courses    |
| GET    | `/courses/{id}/students` | Get students in a course |

---

## 🧠 System Design Flow

1. Client sends request to API
2. FastAPI validates request using Pydantic
3. SQLAlchemy communicates with PostgreSQL
4. Data is stored/retrieved
5. JSON response returned to client

---

## 🚀 Deployment

Deployed using:

* 🌐 Render (Backend Hosting)
* 🐘 PostgreSQL (Database Service)
* ⚙️ Environment Variables for security

---

## 🚀 Future Improvements

* 🔐 JWT Authentication (Login system)
* 🧑‍🏫 Role-based access (Admin/Student)
* ✏️ Update & Delete APIs (Full CRUD expansion)
* 📊 Pagination & filtering
* 🐳 Docker containerization
* 🧪 Automated testing (Pytest)

---

## 👨‍💻 Author

**Pavan Surisetti**

* 🔗 GitHub: [PavanSurisetti GitHub](https://github.com/PavanSurisetti?utm_source=chatgpt.com)
* 🔗 Project Repo: [Student Management System Repo](https://github.com/PavanSurisetti/student-management-system-fastapi?utm_source=chatgpt.com)

---

## 📄 License

This project is licensed under the **MIT License**.
