from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temp connections for performing CRUD operations
Session = sessionmaker(bind=engine)
# map the models to real MySQL tables
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)

  # here we are telling Flask to run close_db whenever a context is destroyed
  app.teardown_appcontext(close_db)

# if this function is called twice in the same route, we dont want to create a second conection
# we want to return the existing connection (which can be saved in Flask app context)
# Flask creates new context every time server request is made (these temp contexts are stored in global variables that can be shared across modules as long as context still active)
# once request ends, the context is removed from the app
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db

# to prevent the app from crashing in production, we want to close the connection to the db once the request officially terminates
def close_db(e=None):
  # if db doens't equal None i.e. db exists, then the pop() method removes db from the g object
  db = g.pop('db', None)

  if db is not None:
    db.close()