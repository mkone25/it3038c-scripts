#This script is meant for the user to input two numbers and they will be returned the prime numbers between them.

#Import the time module for the pause in calculation
import time

#Prompting the user to enter their lower and higher int value
print("Please enter your lower number: ")
lowerNumber = int(input())
print("Please enter your higher number: ")
higherNumber = int(input())

print("Prime numbers bewteen %s and %s are: " % (lowerNumber, higherNumber))

#For loop to determine prime numbers in the range inputed by the user and output the numbers
for num in range(lowerNumber, higherNumber + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            time.sleep(1)
            print(num)