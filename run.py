from app import create_app
from livereloader import web_reloader
from create_admin import ensure_admin
from app.controllers.admin import flask_admin

# Create the Flask application instance using the factory pattern.
# This pattern is useful for creating multiple instances of the app with different configurations.
app = create_app()

# Initialize the Flask-Admin interface.
# This function likely sets up the administrative interface for managing application data.
flask_admin()

# Ensure that an admin user exists in the database.
# This function might check if an admin account is present and create one if it doesn't exist.
ensure_admin()

# Check if the livereloader feature is enabled in the configuration.
# If LIVERELOADER is set to 1 (True) in config.py or .env, the livereloader will be initialized.
# This allows automatic reloading of the application when changes are detected.
if app.config.get("WEB_RELOADER", 0):
    web_reloader()

# The entry point of the application.
# This block ensures that the Flask application runs only if this script is executed directly.
if __name__ == "__main__":
    # Start the Flask development server.
    # The server will listen for incoming HTTP requests on the default port (5000).
    app.run()
