from flask import Flask
from app.routes.home import bp as home
from app.routes.dashboard import bp as dashboard

def create_app(test_config=None):
  # set up app config
  # app should serve any static resources from root directory & not from default /static directory   
  app = Flask(__name__, static_url_path='/')
  # same route will load whether a trailing slash is present  
  app.url_map.strict_slashes = False
  # the app will use this key when creating server-side sessions  
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

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

  return app