from flask import Flask, redirect, request, url_for, render_template
from app import db
from models import User
from app import app
from models import Blogpost, User
from flask_sqlalchemy import SQLAlchemy



@app.route('/home')
def home():
    posts = Blogpost.query.order_by(Blogpost.posted_on.desc()).all()
    return render_template('home.html', posts=posts)
    
@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['post']
        post_author = request.form['author']

        new_post = Blogpost(title=post_title, content=post_content, posted_by=post_author)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('create_post.html')
