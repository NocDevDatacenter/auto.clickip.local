import os
from app.models import Users
from dotenv import load_dotenv
from app import create_app, db
from cryptography.fernet import Fernet

# Load all environment variables from the .env file
load_dotenv()

# Initialize Fernet encryption using the key stored in environment variables
fernet_key = Fernet(os.getenv('MY_FERNET_KEY'))

# Create the Flask application instance
app = create_app()


def ensure_admin():
    """Ensure that an admin user exists in the database."""
    with app.app_context():
        # Retrieve admin credentials from environment variables
        admin_username = os.getenv('ADMIN_USERNAME')
        admin_password = os.getenv('ADMIN_PASSWORD')

        # Raise an error if admin credentials are missing
        if not admin_username or not admin_password:
            raise ValueError("ADMIN_USERNAME or ADMIN_PASSWORD not found in the .env file")

        # Check if the admin user already exists in the database
        auto_noc = Users.query.filter_by(username=admin_username).first()

        # If the admin user does not exist, create and store it securely
        if not auto_noc:
            auto_noc = Users(
                username=admin_username,
                password=fernet_key.encrypt(admin_password.encode('utf-8')),  # Encrypt the password
            )
            db.session.add(auto_noc)
            db.session.commit()
