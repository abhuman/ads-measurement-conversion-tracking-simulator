from attribution.attribution_logic import last_click

def test_last_click():
    events = ["click", "view", "purchase"]
    assert last_click(events) == "purchase"
