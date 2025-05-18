# Notification Service

### Features
- Send Email, SMS, and In-App Notifications
- View User Notification History
- Redis Queue + RQ for Background Processing
- Retry logic can be configured with RQ settings

### Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start Redis server:
   ```
   redis-server
   ```

3. Start FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

4. Start RQ worker:
   ```
   python app/worker.py
   ```

5. API Docs:
   ```
   http://127.0.0.1:8000/docs
   ```

### Assumptions
- SQLite used for simplicity; replace with PostgreSQL if needed.
- Notification sending is mocked (print statements).
