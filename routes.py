from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from models import Blogpost, User


@app.route('/posts', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        create_post()
        return redirect('/posts')
    elif request.Method == 'GET':
        posts = get_posts()
        return render_template('home.html', posts=posts)
    else:
        # return unimplemented error page
        pass


def create_post():
    post_title = request.form['title']
    post_content = request.form['post']
    post_author = request.form['author']

    new_post = Blogpost(title=post_title, content=post_content, posted_by=post_author)

    db.session.add(new_post)
    db.session.commit()


def get_posts():
    posts = Blogpost.query.order_by(Blogpost.posted_on.desc()).all()
    return posts
