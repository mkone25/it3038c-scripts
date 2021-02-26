<<<<<<< HEAD
#!/python

print('What is your name?')
myName = input()
print('Hello,'+ myName+'.That is a good name. How old are you?')
myAge = input()
print(myAge+'? That is funny,I am only a few seconds old.')
print("I wish I was"+myAge*2+"year old" )
=======
import time
start_time=time.time()

print('What is your name?')
myName = input()

# simple while statement
while myName != "MK":
    if myName == "your name":
        print("lol, very funny. Seriously what is your name")
        myName = input()
    else:
        print("Please, tell me your real name")
        myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())

#Simple if statement
if myAge < 13:
    print("Learning young, thant's good")
elif myAge == 13:
    print("You're a teenager now... that's cool, I guess")
elif myAge > 13 and myAge < 30:  
    print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:  
    print("Now you’re adulting.")
else:  
    print("... you’ve lived a long time?")

programAge = int(time.time() - start_time)
print("%s? That is funny, I am only %s seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))
time.sleep(3)
print("I am tired. I go sleep sleep now.")
>>>>>>> 6736d52d66ae24fcc6d1d9256e3fbb91a185ab9e
