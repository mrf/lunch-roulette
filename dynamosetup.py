#!/usr/bin/python
# Creates our DynamoDB table structure

from __future__ import print_function

import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    TableName='People',
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
)

print(response)
