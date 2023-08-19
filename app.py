# I M P O R T S .

from flask import Flask, render_template, redirect, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import *

#App create
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/miniblog'

#App reception
db = SQLAlchemy(app)

#Migrate instantiation
migrate = Migrate(app, db)

#Create table "USER"
class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer,
        primary_key = True
    )

    username = db.Column(
        db.String(100),
        nullable = False,
        unique = True
    )

    password = db.Column(
        db.String(100),
        nullable = False
    )

    email = db.Column(
        db.String(100),
        nullable = False,
        unique = True
    )
    def __str__(self):
        return self.name

#Create table "CATEGORY"
class Category(db.Model):
    __tablename__= 'category'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    
    category_name = db.Column(
        db.String(50), 
        nullable=False
    )

    def __str__(self):
        return self.name

#Create table "POST"
class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(
        db.Integer,
        primary_key= True
    )

    title = db.Column(
        db.String(100),
        nullable= False
    )

    content = db.Column(
        db.Text,
        nullable= False
    )

    date = db.Column(
        db.DateTime,
        nullable= False,
        default= datetime.utcnow
    )

    author_id= db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable= False
    )

    category_id= db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        nullable= False
    )

    def __str__(self):
        return self.name

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(
        db.Integer,
        primary_key= True
    )

    content = db.Column(
        db.Text,
        nullable= False
    )

    date = db.Column(
        db.DateTime,
        nullable= False,
        default= datetime.utcnow
    )
    
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable= False
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
        nullable= False
    )

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_id = request.form['author']
        category_id = request.form['category-post']
        
        new_post= Post(
            title=title,
            content= content,
            author_id = author_id,
            category_id = category_id
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template(
            'index.html'
        )   
def format_text(text):
    formatted_text = text.replace('\n', '<br>')
    return formatted_text

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        new_user = User(username=username,
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('register.html')

@app.context_processor
def inject_posts():
    posts = db.session.query(Post).all()
    formatted_posts = []
    

    for post in posts:
        author = db.session.query(User).get(post.author_id)
        formatted_post = {
            'id': post.id,
            'title': post.title,
            'content': format_text(post.content),
            'author': author.username,
            'date': post.date
        }
        formatted_posts.append(formatted_post)

    return {'posts': formatted_posts}  

@app.context_processor
def inject_users():
    users = db.session.query(User).all()
    return dict(
        users = users
    )

@app.context_processor
def inject_categories():
    categories = Category.query.all()
    return dict(categories=categories)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author_id = request.form['author']
        post.category_id = request.form['category-post']

        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', post=post)

@app.route('/delete/<id>')
def delete_post(id):    
    post = Post.query.get(id)
    Comment.query.filter_by(post_id=id).delete()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/comments/<id>')
def show_comments(id):
    post = Post.query.get(id)
    comments = Comment.query.filter_by(post_id=id).all()

    formatted_comments = []
    for comment in comments:
        author = User.query.get(comment.author_id)
        formatted_comment = {
            'content': comment.content,
            'date': comment.date,
            'author': author.username
        }
        formatted_comments.append(formatted_comment)

    return render_template('comments.html', post=post, comments=formatted_comments)


@app.route('/add-comment', methods=['POST'])
def add_comment():
    content = request.form['content']
    author_id = request.form['author']
    post_id = request.form['post']

    new_comment = Comment(
        content=content,
        author_id=author_id,
        post_id=post_id
    )

    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('index'))

