"""Initialize the Flask application."""
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
app.config.from_object("service.config")

# Add security headers. Disable forced HTTPS for local development and tests.
Talisman(app, force_https=False)

# Allow cross-origin requests to the Accounts API.
CORS(app, resources={r"/accounts/*": {"origins": "*"}})

# Import routes after creating `app` to register the endpoints.
from service import routes  # noqa: E402, F401
