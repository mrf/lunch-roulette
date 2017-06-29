#!/usr/bin/python

from __future__ import print_function

import boto3

client = boto3.client('dynamodb')

table = client.scan(TableName="people")

print(table)
