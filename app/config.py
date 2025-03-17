import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_FILE = "app.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_FILE

SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')
