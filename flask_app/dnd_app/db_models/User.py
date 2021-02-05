from flask_sqlalchemy import SQLAlchemy

def init_user(db):
    class User(db.Model):
        id = db.Column(db.String(30), primary_key=True)
        username = db.Column(db.String(50), nullable=False)
        email = db.Column(db.String(80), unique=True, nullable=False)
        password_hash = db.Column(db.String(50))

        def __repr__(self):
            return f"""<User ID: {self.id}, Username: {self.username}>"""

        def get_characters(self, password):
            """Get the user's characters."""
            pass

        def get_email(self):
            """Get the user's email address."""
            pass

        def check_password(self, password):
            """Check if the password is correct."""
            pass

        def set_email(self, email):
            """Set the user's email address."""
            pass

        def set_password(self):
            """Set password."""
            pass
