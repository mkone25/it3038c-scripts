import time
start_time=time.time()

print('What is your name?')
myName = input()
print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())
programAge = int(time.time() - start_time)
print((myAge, programAge),"? That is funny, I am only a few seconds old.")
print("I wish I was " + str(int(myAge) * 2) + " years old")
time.sleep(3)
print("I am tired. I go sleep sleep now.")