#!/bin/bash

# Get everything up to date
yum update -y

# Get apache + git installed, started up and autostarted on instance restart
yum install httpd git -y
service httpd start
chkconfig httpd on

# Go to our webroot and clone the application code
cd /var/www/html/
git clone https://github.com/mrf/lunch-roulette.git

# Install Python SDK for AWS so we can connect to dynamo
pip install boto3

# Set our default region to avoid confusing later commands
echo "[default]" >> ~/.aws/config
echo "region = us-west-1" >> ~/.aws/config
