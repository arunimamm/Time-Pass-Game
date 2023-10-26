import math
import random
import time

lower=1
upper=100
x=random.randint(lower,upper)
print("welcome to TIME PASS GAME!!!")
name=input("Enter your name: ")
time.sleep(3)
print("Hiii...",name,"\n Your rules for the game TIME PASS")
time.sleep(3)
print(" 1. Guess a number in between 1 and 100 \n 2. If guessed number is greater than a randomly selected number, you wil gets an output 'You guessed high number' \n 3. If guessed number is less than a randomly selected number, you wil gets an output 'You guessed short number' \n 4. If you guessed the correct number, you won the game")
print("You have 10 GUESSES \n ALL THE BEST!! Be the snake...")
time.sleep(3)
count=0

while(count<=10):
    count+=1
    guess=int(input("Enter your guess: "))
    if (guess==x):
        print("Congratulations...You Won in the ",count,"try!!!")
        break
    elif (guess>x):
        print("You guessed high number")
        
    elif (guess<x):
        print("You guessed short number")
else:
    print("You have reached the maximum guess \n The number is %d" % x)
    print("BETTER LUCK NEXT TIME")
