from flask import Flask
from .models import db  # Import the db object initialized in models.py

def create_app(test_config=None):
    """
    Application Factory function to create and configure the Flask app.
    """
    # 1. Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    # Configure the application settings
    app.config.from_mapping(
        SECRET_KEY='dev', 
        # Configure database connection
        SQLALCHEMY_DATABASE_URI='sqlite:///site.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    
    # Optional: Enable auto-reloading for development
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True

    # 2. Initialize database
    # Connect the SQLAlchemy db object to the Flask app
    db.init_app(app)

    # 3. Register Blueprints
    # Import and register the 'main' blueprint from the routes file
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 4. Create database tables within the application context
    with app.app_context():
        # Ensure the Feedback model is imported so SQLAlchemy knows about it
        from . import models 
        db.create_all()  # Create all defined tables in the database

    return app

# The standalone app object definitions at the top have been removed.