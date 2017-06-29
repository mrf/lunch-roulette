#!/usr/bin/python
"""Functions to return values from Dynamo database"""

from __future__ import print_function
import boto3

def full_table():
    """Return all results from Dynamo"""
    client = boto3.client('dynamodb', region_name='us-west-1')
    response = client.scan(TableName="People")
    return response['Items']
