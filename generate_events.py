import random, datetime, json

def generate():
    return {
        "user_id": random.randint(1000,9999),
        "event_type": "click",
        "timestamp": datetime.datetime.now().isoformat(),
        "campaign_id": "CAMP123",
        "value": 0
    }

print(json.dumps(generate()))
