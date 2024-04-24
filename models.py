from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class j4EmailAddress(db.Model):
    __tablename__ = "Email_Farming"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, email):
        self.email = email
 
    def __repr__(self):
        return f"{self.email}"