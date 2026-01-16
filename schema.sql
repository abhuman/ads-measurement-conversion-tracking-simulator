CREATE TABLE ad_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT,
  event_type TEXT,
  timestamp TEXT,
  campaign_id TEXT,
  value FLOAT
);
