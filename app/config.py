import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the database file name
DATABASE_FILE = "app.db"

# Set the SQLAlchemy database URI using SQLite
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_FILE

# Load the secret key from environment variables for security purposes
SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')
