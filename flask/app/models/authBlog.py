
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from app import db
from .blogEntry import BlogEntry


class PrivateBlog(BlogEntry, UserMixin, SerializerMixin):
    owner_id = db.Column(db.Integer, db.ForeignKey('auth_blogs.id'))

    def __init__(self, name, message, email, owner_id):
        super().__init__(name, message, email)
        self.owner_id = owner_id


class AuthBlog(db.Model, UserMixin):
    __tablename__ = "auth_blogs"
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    avatar_url = db.Column(db.String(100))

    def __init__(self, email, name, password, avatar_url):
        self.email = email
        self.name = name
        self.password = password
        self.avatar_url = avatar_url
