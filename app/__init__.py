from flask_admin import Admin, AdminIndexView
from livereload import Server  # noqa: F401
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template
from sqlalchemy.orm import DeclarativeBase
import importlib

#def run_unauthorizedadmin2():
   # call (["python", "unauthorizedadmin.py"])

#run_unauthorizedadmin2()
    
    
# Declarative base class for SQLAlchemy
# This class serves as the base for all SQLAlchemy models, enabling table creation in the database.
class Base(DeclarativeBase):
    pass


# Initializing Flask extensions
db = SQLAlchemy(model_class=Base)  # Manages database interactions
lm = LoginManager()                # Manages user sessions and authentication
migrate = Migrate()                # Manages database migrations



#unauthorizedadmin = importlib.import_module("unauthorizedadmin.py")

 #Custom admin index view to restrict access
class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
       """Allow access only to authenticated users."""
       return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        """Redirect to login page if user is not authenticated."""
        return render_template("admin/admin_access_error.html")


#Flask-Admin instance with secured access

admin = Admin(index_view=SecureAdminIndexView())


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')  # Loads configuration from the config.py file

    # Initializing extensions with the Flask application context
    db.init_app(app)           # Sets up SQLAlchemy with the application
    lm.init_app(app)           # Sets up the login manager
    admin.init_app(app)        # Sets up the administrative interface
    migrate.init_app(app, db)  # Sets up database migration

    # Login configurations
    lm.login_view = 'auth.login'  # Defines the default login route
    lm.login_message = 'Please log in to access this page.'  # Message displayed when accessing a protected page without logging in
    lm.login_message_category = 'info'  # Category of the login message
    lm.session_protection = "strong"  # Level of session protection

    lm.refresh_view = "auth.login"  # Route for reauthentication
    lm.needs_refresh_message = (
        u"To protect your account, please reauthenticate to access this page."
    )  # Message displayed when reauthentication is needed
    lm.needs_refresh_message_category = "info"  # Category of the reauthentication message

    # Blueprint registration
    from app.controllers.blueprints import register_blueprints
    register_blueprints(app)  # Registers all configured blueprints

    with app.app_context():
        db.create_all()  # Creates all tables in the database if they do not exist

    # Basic route for the home page
    @app.route('/')
    def page_home():
        return redirect(url_for('int_summary_bp.interface_summary'))  # Redirects to the network interface summary page

    return app  # Returns the configured Flask application instance
