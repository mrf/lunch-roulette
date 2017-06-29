#!/usr/bin/python
"""Functions to return values from Dynamo database"""

from __future__ import print_function
import boto3

CLIENT = boto3.client('dynamodb', region_name='us-west-1')

def full_table():
    """Return all results from Dynamo and clean up"""
    response = CLIENT.scan(TableName="People")
    listing = []
    for item in response['Items']:
        listing.append(item['name']['S'])
    return listing
