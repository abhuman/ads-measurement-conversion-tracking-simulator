def detect_duplicates(events):
    seen = set()
    duplicates = []
    for e in events:
        key = (e["user_id"], e["timestamp"])
        if key in seen:
            duplicates.append(e)
        seen.add(key)
    return duplicates
