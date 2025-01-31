from api import app, db

# Create the database and the tables
with app.app_context():
    db.create_all()
