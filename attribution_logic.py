def last_click(events):
    return events[-1]

def linear(events):
    weight = 1 / len(events)
    return [{"event": e, "weight": weight} for e in events]

def time_decay(events):
    total = sum(range(1, len(events) + 1))
    return [{"event": e, "weight": (i+1)/total} for i, e in enumerate(events)]
