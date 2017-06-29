#!/usr/bin/python
"""Functions to return values from Dynamo database"""

from __future__ import print_function
import boto3

def full_table():
    """Return all results from Dynamo"""
    client = boto3.client('dynamodb')
    response = client.scan(TableName="People")
    # TODO return as a clean object
    return response['Items']
