#!/bin/bash
yum update -y
yum install httpd git -y
service httpd start
chkconfig httpd on
cd /var/www/html/
git clone https://github.com/mrf/lunch-roulette.git
