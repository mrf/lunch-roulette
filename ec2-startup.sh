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

# Install Python SDK for AWS
pip install boto3
