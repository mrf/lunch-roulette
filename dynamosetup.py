#!/bin/python2
# Creates our DynamoDB table structure

import boto.dynamodb2

from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table

people = Table.create('people', schema=[
    HashKey('username'), # defaults to STRING data_type
])

print('created table people')
