from app import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone


class BlogEntry(db.Model, SerializerMixin):
    __tablename__ = "blog_entries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(280))
    email = db.Column(db.String(50), unique=True)
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)

    def __init__(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email
        self.date_created = datetime.now(timezone.utc)

    def update(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email
        self.date_updated = datetime.now(timezone.utc)
