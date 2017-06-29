#!/usr/bin/python

from __future__ import print_function
try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest
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

print("<h2>{} people showed up to lunch today.</h2>".format(COUNT))

GROUPCOUNT = COUNT / 5
print("Should be {} groups".format(GROUPCOUNT))

MINGROUPSIZE = 3
MAXGROUPSIZE = 5

# Use itertools library to chunk our list
CHUNKED_LIST = list(zip_longest(fillvalue='', *[iter(RANDOMIZED)]*5))

print('    <ul>')
# TODO some  groups are too small
for group in CHUNKED_LIST:
    print('      <li>{}</li>'.format(group))
print('    </ul>')
print("  </body>")
print("</html>")
