def validate_events(events):
    return all("timestamp" in e and "user_id" in e for e in events)
