from flask import Blueprint, render_template, request, redirect, url_for
# Import db and the Feedback model from your application's models file
from .models import db, Feedback 

# Create a Blueprint object
main = Blueprint("main", __name__)

@main.route("/")
def home():
    """Renders the main page."""
    # You could optionally pass all existing feedback to the template here
    # feedback_list = Feedback.query.all()
    # return render_template("index.html", feedback=feedback_list)
    return render_template("index.html")

# --- NEW ROUTE FOR HANDLING FEEDBACK SUBMISSION ---
@main.route("/feedback", methods=["POST"])
def submit_feedback():
    """
    Handles the form submission, saves data to the database, and redirects.
    """
    # Check if the request is a POST (which it should be, based on the decorator)
    if request.method == 'POST':
        try:
            # 1. Get data from the submitted form (keys match 'name' attributes in HTML)
            customer_name = request.form.get('name')
            star_rating = request.form.get('rating')
            comment_text = request.form.get('comments')
            
            # Simple validation check
            if not all([customer_name, star_rating, comment_text]):
                # Handle missing data, perhaps with a flash message
                return redirect(url_for('main.home')) 

            # 2. Create a new Feedback object
            new_feedback = Feedback(
                name=customer_name,
                rating=int(star_rating), # Convert rating to integer
                comments=comment_text
            )

            # 3. Add to session and commit to the database
            db.session.add(new_feedback)
            db.session.commit()
            
            # 4. Redirect to the home page (Post/Redirect/Get pattern)
            # You could redirect to a separate 'thank you' page if desired
            return redirect(url_for('main.home'))

        except Exception as e:
            # Log the error and rollback the database session on failure
            print(f"Database error during feedback submission: {e}")
            db.session.rollback()
            # In a production app, use 'flash' to show the error
            return "An error occurred while saving your feedback.", 500

    # Fallback in case of direct GET request to /feedback
    return redirect(url_for('main.home'))