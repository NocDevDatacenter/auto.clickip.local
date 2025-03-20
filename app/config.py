import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the database file name
DATABASE_FILE = "nexus.database"

# Set the SQLAlchemy database URI using SQLite
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_FILE

# Load the secret key from environment variables for security purposes
SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')

# Enables or disables the web reloader (LiveReloader) based on the environment variable.
# Set WEB_RELOADER=1 in the .env file to enable automatic reloading during development.
# Defaults to 0 (disabled) if not set.
WEB_RELOADER = int(os.getenv('WEB_RELOADER', 0))
