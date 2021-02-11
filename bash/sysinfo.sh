#!/bin/bash
#this script will email our IP address, hostname and today's date
emailaddress=konemu@mail.uc.edu
today=$(date +"%d-%m-%Y")
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
content="User: $USER
Server name is: $HOSTNAME
IP address is: $ip
Date and Time is: $today"
echo "Email will content: $content"
mail -s "IT3038C LINUX IP" $emailaddress <<<$(echo -e $content)
