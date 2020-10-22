from app import app, db
from flask import render_template, flash, redirect, url_for
from app.form import CommentForm
from app.models import User, Comment

@app.route('/', methods = ['GET', 'POST'])
@app.route('/comments', methods = ['GET', 'POST'])
def comments():
    form = CommentForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)        
        post = Comment(body = form.comment.data, author = user)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('comments'))  
    posts = Comment.query.order_by(Comment.timestamp.desc()).all()
    return render_template('comments.html', title = 'Comment', form = form, posts = posts)     