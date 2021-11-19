from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

# corresponds to Router middleware of Express.js
bp = Blueprint('home', __name__, url_prefix='/')

# this decorator turns the function into a route
@bp.route('/')
def index():
  # get all posts
  # this function returns a session connection that's tied to this route's context
  db = get_db()
  # now query on the connection object
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
    'homepage.html', 
    posts=posts,
    loggedIn=session.get('loggedIn')
  )

@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')

# <id> = parameter syntax
@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  # filter method specifies SQL WHERE clause & we end with .one instead of .all
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )