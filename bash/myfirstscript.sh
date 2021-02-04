#!/bin/bash
#THis script outputs the IP address and hostname of a machine

greeting="This is a script, Hello"
echo "greeting, thanks for joining us! You owe me \$20"
echo Machine: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME
a=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
echo "My IP is: $a"
