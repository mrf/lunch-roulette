#!/bin/bash

# Get everything up to date
yum update -y

# Get apache + git installed
yum install httpd git -y

# Write basic python config for apache
echo "<Directory /var/www/html/lunch-roulette>" >> /etc/httpd/conf.d/python.conf
echo "    Options +ExecCGI" >> /etc/httpd/conf.d/python.conf
echo "    AddHandler cgi-script .py" >> /etc/httpd/conf.d/python.conf
echo "    DirectoryIndex index.py" >> /etc/httpd/conf.d/python.conf
echo "</Directory>" >> /etc/httpd/conf.d/python.conf

# Get apache started up and auto-restarted on instance restart
service httpd start
chkconfig httpd on

# Go to our webroot and clone the application code
cd /var/www/html/
git clone https://github.com/mrf/lunch-roulette.git

# Set permissions to executable
chmod +x index.py

# Install Python SDK for AWS so we can connect to dynamo
pip install boto3

# Set our default region to avoid confusing later commands
echo "[default]" >> ~/.aws/config
echo "region = us-west-1" >> ~/.aws/config
