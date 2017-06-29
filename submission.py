#!/usr/bin/python

from __future__ import print_function

import boto3

client = boto3.client('dynamodb')

response = client.put_item(
    TableName="People",
    Item={
        'name': {
            'S': 'Foo',
        }
    },
    ReturnConsumedCapacity='TOTAL',
)

print(response)
