#!/usr/bin/python
"""Functions to return values from Dynamo database"""

from __future__ import print_function
import boto3

CLIENT = boto3.client('dynamodb', region_name='us-west-1')

USER = 'Frank'

RESPONSE = CLIENT.put_item(
    TableName="People",
    Item={
        'name': {
            'S': USER,
        }
    },
    ReturnConsumedCapacity='TOTAL',
)

print(RESPONSE)

# Set our document type so that CGI can render it
print("Content-Type: text/html\n\n")

print("<html>")
print("  <head>")
print('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
print("  </head>")
print("  <body>")
print("     <h1>Please Insert a User</h1>")
print('     <form action="/newuser.py">Name:<input type="text" name="name"></form>')
print("  </body>")
print("</html>")
