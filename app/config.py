import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present).
# Used for sensitive or environment-specific configurations (e.g., API keys, database URIs).
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path, override=True)

# Default port for the Flask development server.
# Can be overridden by environment variables or deployment settings (e.g., Heroku uses PORT env var).
APLICATION_PORT = 5000

# SQLite database filename.
# Stores application data in a local file (default: 'nexus.db').
DATABASE_FILE = 'nexus.db'

# SQLAlchemy database connection URI.
# Uses SQLite for local development (file-based database).
# Format: 'sqlite:///<database_file_path>'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE

# Secret key for Flask session encryption and security features.
# Loaded from environment variables for production safety.
# Warning: Never hardcode secrets in version control!
SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')

# Enable/disable the LiveReload server for frontend development.
# True: Auto-refreshes browser on file changes (HTML/CSS/JS).
# False: Disabled (default for production).
WEB_RELOADER = False

# SSH port for connecting to the device (default is 22)
NETMIKO_PORT = 22

# General timeout for the connection attempt (in seconds)
NETMIKO_TIMEOUT = 30

# Maximum session timeout before disconnecting the SSH session (in seconds)
NETMIKO_SESSION_TIMEOUT = 60
