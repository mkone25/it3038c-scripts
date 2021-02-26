#!/bin/bash
#This script, when run will tell the user the date and time 

date=$(date +"%m-%d-%Y")
echo "Today's Date: $date"
user=$(who)
echo "Current user logged on: $user"
time=$(date +"%T")
echo "Exact time that the script is run is: $time"
ls -l
echo "Have a Great Day!!!!!!!"
