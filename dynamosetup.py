#!/usr/bin/python
# Creates our DynamoDB table structure

from __future__ import print_function

import boto3

client = boto3.client('dynamodb')

"""
people_response = client.create_table(
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
"""

groups_response = client.create_table(
    TableName='Groups',
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N',
        },
        {
            'AttributeName': 'Members',
            'AttributeType': 'SS',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Members',
            'KeyType': 'HASH',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
)

#print(people_response)
print(groups_response)
