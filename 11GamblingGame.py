import random
import time

# Finds two random numbers each between 0 and 5
Rnum1 = random.randint(1, 4)
Rnum2 = random.randint(1, 4)
print("Welcome to Gambling game")
print("If the two random numbers generated by computer are same you win!")
# user can ony play if they approve to
a = input("Type YES if you want to play : ")
if a == "YES":
    print("Let's begin")
else:
    print("Get out")
print("Please wait 10 seconds while I declare the results")
time.sleep(10)
if a == "YES" and Rnum1 == Rnum2:
    print("You win!")
else:
    print("You loose")
# determines the results

