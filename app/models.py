from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy without passing app
db = SQLAlchemy()

class Feedback(db.Model):
    """Database model for storing customer feedback and ratings."""
    # Define the table name
    __tablename__ = 'feedback'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Stores the 1-5 star rating
    comments = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Feedback {self.name} - {self.rating} stars>'