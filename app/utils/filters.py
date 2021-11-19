# formatting date
def format_date(date):
  return date.strftime('%m/%d/%y')

# verifying datetime filter functions correctly
from datetime import datetime
print(format_date(datetime.now()))

# removes extraneous info from URL string, leaving only domain name
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# verifying url filter functions correctly
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))

# pluralizes 'comment' if there is more than 1
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# plural test
print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))