from flask import Flask
from app.routes.home import bp as home
from app.routes.dashboard import bp as dashboard
from app.routes.api import bp as api
from app.db import init_db
from app.utils import filters

def create_app(test_config=None):
  # set up app config
  # app should serve any static resources from root directory & not from default /static directory   
  app = Flask(__name__, static_url_path='/')
  # same route will load whether a trailing slash is present  
  app.url_map.strict_slashes = False
  # the app will use this key when creating server-side sessions 
  # in production environment, change key to something harder to guess 
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural

  # same as app.get('/hello', (req, res) => {
  #     res.send('hello world');
  # });
  # when using Express.js
  @app.route('/hello')
  def hello():
    return 'hello world'

  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.register_blueprint(api)
  
  # passing in the app context variable when we intialize the connection to the db
  # how we ensure connections will not remain open and potentially locking up the server
  init_db(app)

  return app