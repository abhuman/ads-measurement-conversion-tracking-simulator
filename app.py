from flask import Flask
from flask_cors import CORS
from routes.event_routes import event_bp
from routes.conversion_routes import conversion_bp
from routes.health_routes import health_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_bp)
app.register_blueprint(conversion_bp)
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
