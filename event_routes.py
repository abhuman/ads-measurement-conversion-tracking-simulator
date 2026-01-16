from flask import Blueprint, request, jsonify
from services.event_processor import process_event

event_bp = Blueprint("events", __name__)

@event_bp.route("/events", methods=["POST"])
def ingest_event():
    data = request.json
    process_event(data)
    return jsonify({"status": "event_ingested"})
