from flask import Blueprint, render_template

# corresponds to Router middleware of Express.js
bp = Blueprint('home', __name__, url_prefix='/')

# this decorator turns the function into a route
@bp.route('/')
def index():
  # whatever function returns becomes the response
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

# <id> = parameter syntax
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')