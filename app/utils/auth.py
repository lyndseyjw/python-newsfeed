from flask import session, redirect
from functools import wraps

# a decorator intended to return a new function
def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      # 2 arguments ensure no matter how many arguments are given, wrapped_function captures them all
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function



# when used, looks like this : 
# @login_required
# def callback():
#   print('hello')

# callback() # prints 'wrapper', then 'hello'


# printing callback.__name__ prints wrapped_function



# same as writing this in JS: 
# function login_required(func) {
#   function wrapped_function() {
#     console.log('wrapper');

#     // func(*args, **kwargs)
#     return func(...arguments);
#   }

#   return wrapped_function;
# }

# // @login_required
# // def callback():
# const callback = login_required(() => {
#   console.log('hello');
# });

# callback();