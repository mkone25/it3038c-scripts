#!/bin/bash
#This script will tell you the date the time it was run and the files that are in your directory plus who is logged on the system

date=$(date +"%m-%d-%Y")
echo "Today's Date is: $date"
user=$(who)
echo "The user that is loggeed on is: $user"
time=$(date +"%T")
echo "the exact time that the script was ran is: $time"
ls -l
echo "That's all the information I can provide for now!!!!"