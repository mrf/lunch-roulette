#!/usr/bin/python

from __future__ import print_function
import boto3

def full_table():
    client = boto3.client('dynamodb')
    response = client.scan(TableName="People")
    return response
