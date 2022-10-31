from app import db
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Blogpost(UserMixin, db.Model):
     __tablename__ = "user"

     id = db.Column(db.Integer(), primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     posted_by = db.Column(db.String(20), nullable=False, default='N/A')
     posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

     def __repr__(self):
        return self.title

db.create_all()
db.session.commit()

