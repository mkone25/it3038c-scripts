Project 2

This project is a script that will ask the user to input two numbers and the prime numbers between those two numbers will be returned.

In python

First, import the time module which will be used at the end of the script to give  the result one second difference of each other.

    import time

Next, the user will be prompted to input two numbers, the lower number first then the higher number.

        print("Please enter your lower number: ")
        lowerNumber = int(input())
        print("Please enter your higher number: ")
        higherNumber = int(input())

Next is a for loop that will calculate the prime numbers in the range. Using the range feature, 1 is added to the higher value because it doesn't count it. Prime numbers must be greater than one so we test if the numbers in the range are divisible by any number 2 through the rest of the range.

    for num in range(lowerNumber, higherNumber + 1):
        if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            time.sleep(1)
            print(num)

With that, any two numbers that the user want to determine their prime number will be found.