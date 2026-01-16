from flask import Blueprint, jsonify
from services.roi_calculator import calculate_roi

conversion_bp = Blueprint("conversion", __name__)

@conversion_bp.route("/roi")
def roi():
    return jsonify({"roi": calculate_roi(1000, 400)})
