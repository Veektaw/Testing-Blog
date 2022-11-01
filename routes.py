from crypt import methods
from curses import flash
from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from models import Blogpost, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin


##### This is supposed to show all posts that have been created ######
###### If none has been posted, i will use jinja syntax to tell user to log in so they can post #######
@app.route("/")
def home():
    posts = Blogpost.query.order_by(Blogpost.posted_on.desc()).all()
    return render_template('home.html', posts=posts)


##### This is to create a new post ######
#### Not entirely sure i've done the right thing #####
@app.route("/create_post/new", methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['post']
        post_author = request.form['author']

        new_post = Blogpost(title=post_title, content=post_content, posted_by=post_author)

        db.session.add(new_post)
        db.session.commit()

        #### This redirects the user back to the homepage when they post the blog ####
        return redirect('home.html', posts=posts)

    #### need clarification where this is directed #####
    elif request.method == 'GET':
        posts = get_posts()
        return redirect('home.html', posts=posts)


    #### need clarification where this is directed #####
    else:
        pass
    return render_template('create_post.html')

#### This is supposed to bring out posts when they are CLICKED on ######
def get_posts():
    posts = Blogpost.query.order_by(Blogpost.posted_on.desc()).all()
    return posts

##### This is supposed to edit(UPDATE) an already posted blog ####
@app.route("/edit_blog/<int:id/")
def edit_blog(id):
    blog = Blogpost.query.filter_by(id=id).first()
    blog.complete = not blog.complete

    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('home'))


#### This is to delete a blog ####
@app.route("/delete/<int:id/")
def edit_blog(id):
    blog = Blogpost.query.filter_by(id=id).first()
    blog.complete = not blog.complete

    db.session.commit()
    return redirect(url_for('home'))


### This is to sign up ####
@app.route("/signup", methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
            fullname = request.form.get('fullname')
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if user:
                flash('Username already in use')
                return redirect(url_for('register'))

            email_exists = User.query.filter_by(email=email).first()
            if email_exists:
                flash('Email already in use')
                return redirect(url_for('register'))

            password = generate_password_hash(password)

            new_user = User(fullname=fullname, username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('signup'))

        return render_template('signup.html')

##### This is to sign in user ######
@app.route("/signin")
def signin():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        login_user(user)
    else:
        flash('Credentials do not match')

        return redirect(url_for('home'))

    return render_template('signin.html')


##### This is to log out the user ######
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


############ This is supposed to bring out posts when you click on them, is it now under, 'create_post'? #######
############ If i remember correctly, the method is to get posts by 'id' #######
#@app.route("/post")
#def view_blogs():
    #posts = Blogpost.query.order_by(Blogpost.posted_on.desc()).all()
    #return posts


#### This is supposed to send it back to homepage when the user clicks submit, not sure i got it right #####
@app.route("/contact", methods=['POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('home')) 

#### These is fine ####
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)