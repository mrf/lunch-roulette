#!/usr/bin/python
"""Landing page for application"""

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

print("<html>")
print("  <head>")
print('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
print("  </head>")
print("  <body>")
print("     <h1>Welcome to Lunch Roulette!</h1>")
print('     <a href="newuser.py">Create new user</a>')

# Pull in our full list from Dynamo
EVERYONE = listing.full_table()
COUNT = len(EVERYONE)
# Randomize the list before we break it up
RANDOMIZED = random.sample(EVERYONE, COUNT)

print("     <h2>{} people showed up to lunch today.</h2>".format(COUNT))

MINGROUPSIZE = 3
MAXGROUPSIZE = 5

# TODO turn following into button and save into Dynamo

# Use itertools library to chunk our list
CHUNKED_LIST = list(zip_longest(fillvalue='<<>>', *[iter(RANDOMIZED)]*5))

print('     <ul>')

# Checking to see if we have and groups that are too small
for i, group in enumerate(CHUNKED_LIST):
    if group.count('<<>>') > 2:
        new_group = list(group)
        # And back to tuple as we save
        CHUNKED_LIST[i] = tuple(new_group)
        # Group 0 is never to small so we steal from there
        source_group = list(CHUNKED_LIST[0])

        # Its a Tuple so we have to make editable
        new_group = list(group)

        # Check how many we need to move around
        if group.count('<<>>') == 4:
            new_group[2], source_group[1] = source_group[1], new_group[2]
            new_group[3], source_group[2] = source_group[2], new_group[3]
        elif group.count('<<>>') == 3:
            new_group[2], source_group[1] = source_group[1], new_group[2]

        # Convert back to tuple so we don't lose in this execution
        CHUNKED_LIST[i] = tuple(new_group)
        CHUNKED_LIST[0] = tuple(source_group)

for group in CHUNKED_LIST:
    print('      <li>')
    print('      <ul>')

    for person in group:
        print('          <li>{}</li>'.format(person))

    print('      </ul>')
    print('      </li>')
print('    </ul>')
print("  </body>")
print("</html>")
