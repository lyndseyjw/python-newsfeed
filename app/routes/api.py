# allows us to see error message if except statement called
import sys
from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
  # mechanism to capture data sent in POST
  # request global contextual object that contains info about the request
  data = request.get_json()
  # db connection logic
  db = get_db()
  
  try:
    # create a new user
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )

    # save in database
    # db.add method preps INSERT statement
    db.add(newUser)
    # method officially updates db
    db.commit()
    print('success!')
  except:
    # allows us to see error message if except statement called
    print(sys.exc_info()[0])
    # if db.commit fails, connection will remain in pending state, which can result in app crashes in production environment
    db.rollback()
    # insert failed, so send error to front end
    return jsonify(message = 'Signup failed'), 500

  # setting up session so app knows user is logged in
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True

  return jsonify(id = newUser.id)

  # can add the following except statements to specifically print errors
  # AssertionError thrown when custom validations fail
  # except AssertionError:
  #   print('validation error')
  # IntegrityError thrown when something specific to MySQL (like UNIQUE constraint) fails
  # except sqlalchemy.exc.IntegrityError:
  #   print('mysql error')

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'), 400
  
  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400

  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)