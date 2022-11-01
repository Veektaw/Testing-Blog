from blog import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "User"

    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Blogpost(UserMixin, db.Model):
     __tablename__ = "Blogpost"


     id = db.Column(db.Integer(), primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     content = db.Column(db.Text(), nullable=False)
     posted_by = db.Column(db.String(20), nullable=False, default='N/A')
     posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

     def __repr__(self):
        return f'<User {self.title}>'

db.session.commit()
db.create_all()
