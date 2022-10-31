from flask import Flask, redirect, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime


#base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

# Why are these in app and in models.py?
class User(UserMixin, db.Model):
    __tablename__ = "User"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fullname = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Blogpost(UserMixin, db.Model):
     __tablename__ = "Blogpost"

     id = db.Column(db.Integer(), primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     content = db.Column(db.String(10000), nullable=False)
     posted_by = db.Column(db.String(20), nullable=False, default='N/A')
     posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

     def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/blogs")
def create_blog():
    return render_template('blog.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
