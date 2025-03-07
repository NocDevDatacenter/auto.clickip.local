from app import create_app
from app.controllers.admin import flask_admin
from create_admin import ensure_admin

# Create the Flask application instance using the factory pattern.
# This pattern is useful for creating multiple instances of the app with different configurations.
app = create_app()

# Initialize the Flask-Admin interface.
# This function likely sets up the administrative interface for managing application data.
flask_admin()

# Ensure that an admin user exists in the database.
# This function might check if an admin account is present and create one if it doesn't exist.
ensure_admin()

# The entry point of the application.
# This block ensures that the Flask application runs only if this script is executed directly.
if __name__ == "__main__":
    # Start the Flask development server.
    # The server will listen for incoming HTTP requests on the default port (5000).
    app.run()
