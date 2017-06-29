#!/usr/bin/python

from __future__ import print_function
import requests

# Set our document type so that CGI can render it
print("Content-Type: text/html\n\n")

# TODO: Multiline print would look cleaner
print("<html>")
print("  <head>")
print('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
print("  </head>")
print("  <body>")
print("     <h1>Welcome to Lunch Roulette!</h1>")

listing = requests.get('http://localhost/lunch-roulette/listing.py', allow_redirects=True)

print("  </body>")
print("</html>")
