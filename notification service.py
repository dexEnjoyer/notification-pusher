import sqlite3
from datetime import datetime
import time
import random

# --- DB Setup ---
def connect_db():
    return sqlite3.connect("notifications.db")

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            message TEXT,
            timestamp TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

# --- Simulated Queue Processing with Retry ---
def process_notification_with_retry(user_id, notif_type, message, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            # Simulate 30% chance of failure
            if random.random() < 0.3:
                raise Exception("Simulated send failure.")

            # Simulated delivery
            print(f"✅ Delivered [{notif_type.upper()}] to User {user_id}: {message}")
            save_notification(user_id, notif_type, message, "delivered")
            return

        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed: {e}")
            attempt += 1
            time.sleep(delay)

    print("❌ All retries failed.")
    save_notification(user_id, notif_type, message, "failed")

# --- Save Notification to DB ---
def save_notification(user_id, notif_type, message, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notifications (user_id, type, message, timestamp, status)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, notif_type, message, timestamp, status))
    conn.commit()
    conn.close()

# --- Retrieve Notifications ---
def get_notifications():
    user_id = int(input("Enter User ID to retrieve notifications: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notifications WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No notifications found.")
        return

    print(f"\n📨 Notifications for User {user_id}:")
    for row in rows:
        print(f"[{row[4]}] {row[2].upper()} | {row[3]} | Status: {row[5]}")

# --- Menu Interface ---
def menu():
    setup_db()
    while True:
        print("\n=== Notification Service ===")
        print("1. Send Notification")
        print("2. Get User Notifications")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_id = int(input("User ID: "))
            notif_type = input("Type (email/sms/in-app): ").lower()
            if notif_type not in ["email", "sms", "in-app"]:
                print("Invalid type.")
                continue
            message = input("Message: ")
            process_notification_with_retry(user_id, notif_type, message)
        elif choice == "2":
            get_notifications()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

# --- Entry Point ---
if __name__ == "__main__":
    menu()
