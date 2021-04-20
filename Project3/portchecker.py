#!/usr/bin/python

#import socket and time
import socket
import time

#Enter the site you want to check and port to the port number you want to check.
#ip = "espn.com"
#port = 80

ip = input("Enter the website you would like to check, domain name, like www.google.com: ")
port = input("Enter the port number you would like to check, like port 80 for http: ")
retry = 2
timeout= 3

def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def checkHost(ip, port):
        ipup = False
        if isOpen(ip, port):
            ipup = True

        else:
            print ("Port " + str(port) + " on " + ip + " is CLOSED")

        return ipup

if checkHost(ip, port):
       print ("Port " + str(port) + " on " + ip + " is Open")