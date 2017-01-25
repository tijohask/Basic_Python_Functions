#import the proper library
from urllib.request import urlopen

#retrieve and read the url page from the internet
page = urlopen("http://example.com")

#print it out to the end user
print(page.read())
