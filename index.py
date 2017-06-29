#!/usr/bin/python

from __future__ import print_function
import sys
import listing

# Set our document type so that CGI can render it
print("Content-Type: text/html\n\n")

# TODO: Multiline print would look cleaner
print("<html>")
print("  <head>")
print('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
print("  </head>")
print("  <body>")
print("     <h1>Welcome to Lunch Roulette!</h1>")
print('<pre>')

#try:
EVERYONE = listing.full_table()
#except:
#    print("<p>Error: %s</p>" % str(Exception))

for person in EVERYONE:
    print(person)

print('</pre>')
print("  </body>")
print("</html>")
