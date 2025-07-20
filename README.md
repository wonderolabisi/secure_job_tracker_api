# Secure Job Tracker API

A secure job tracking backend built with FastAPI, SQLite, and JWT authentication.

## 🔐 Features
- User registration & login
- JWT-protected job endpoints
- CRUD for job listings
- SQLite support for lightweight storage

## 📦 Tech Stack
- Python & FastAPI
- SQLite & SQLAlchemy
- JWT (python-jose)
- Pydantic
- Passlib (bcrypt)

## 🧪 Local Setup

```bash
git clone https://github.com/wonderolabisi/secure_job_tracker_api.git
cd secure_job_tracker_api
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
