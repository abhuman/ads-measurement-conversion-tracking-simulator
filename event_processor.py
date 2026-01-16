from database import get_db

def process_event(event):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO ad_events VALUES (NULL, ?, ?, ?, ?, ?)",
        (
            event["user_id"],
            event["event_type"],
            event["timestamp"],
            event["campaign_id"],
            event.get("value", 0)
        )
    )
    db.commit()
