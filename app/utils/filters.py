def format_date(date):
    return date.strftime("%d %b %Y")

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    
    return word

# test filters
# test format_date filter
from datetime import datetime
print(format_date(datetime.now()))

#test format_url filter
print(format_url('http://www.google.com/helloworld'))
print(format_url('https://www.google.com/search?q=hello+world'))

# test format_plural filter
print (format_plural(2, 'cat'))
print (format_plural(1, 'dog'))



