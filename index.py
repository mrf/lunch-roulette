#!/usr/bin/python

from __future__ import print_function
import random
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

# Pull in our full list from Dynamo
EVERYONE = listing.full_table()
COUNT = len(EVERYONE)
# Randomize the list before we break it up
RANDOMIZED = random.sample(EVERYONE, COUNT)

print("{} people showed up to lunch today.".format(COUNT))

GROUPCOUNT = COUNT / 5
print(GROUPCOUNT)

print('<pre>')
for person in RANDOMIZED:
    print(person)

print('</pre>')
print("  </body>")
print("</html>")
