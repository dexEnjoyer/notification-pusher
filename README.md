# 🚀 Notification Service

A backend service for sending and retrieving notifications via **Email**, **SMS**, or **In-App**, with support for **background processing** using Redis Queue (RQ).

---

## 📌 Features

- ✅ REST API to send notifications
- ✅ Retrieve notifications for a specific user
- ✅ Asynchronous task processing via Redis Queue (RQ)
- ✅ Extensible for retries and failure handling

---

## 📁 Folder Structure

```
notification-service/
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # SQLAlchemy DB models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB session + config
│   ├── notifications.py   # Notification sending logic
│   └── worker.py          # RQ worker to process jobs
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd notification-service
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Redis Server

Make sure Redis is installed and running:

```bash
# macOS
brew install redis && brew services start redis

# Ubuntu/Debian
sudo apt install redis && sudo service redis start

# Windows
Download from https://github.com/microsoftarchive/redis/releases
```

Test it:
```bash
redis-cli ping  # Should return "PONG"
```

### 5. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

### 6. Start the Background Worker

In a **new terminal**, run:

```bash
python app/worker.py
```

---

## 🧪 Example API Usage

### ✅ Send a Notification

**POST** `/notifications`

```json
{
  "user_id": 1,
  "message": "Your OTP is 123456",
  "type": "sms"
}
```

### 📄 Get Notifications for a User

**GET** `/users/1/notifications`

---

## 💡 How It Works

- When a user sends a notification, it is stored in the DB with `pending` status.
- A background worker reads jobs from the Redis queue.
- It updates the status to `sent` after simulating delivery.

---

## 🛠️ Technologies Used

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database operations
- **Redis + RQ** – Queueing system for background tasks
- **SQLite** – Lightweight default DB (can be changed to PostgreSQL)

---

## 🧩 Future Improvements

- Add retry mechanism for failed notifications
- Add support for real email/SMS APIs (e.g., Twilio, SendGrid)
- Dockerize the service
