from tkinter import *
window=Tk()
window.title("Time Pass Game")
window.geometry("250x250")
import random
import math
import time
def game():
    lower=1
    upper=100
    x=random.randint(lower,upper)
    label=Label(window,text="WELCOME TO TIME PASS GAME!!!")
    #print("WELCOME TO TIME PASS GAME!!!")
    userlabel=Label(window,text='Enter your name : ')
    userEntry=Entry(window)
    #name=input('Enter your name : ')
    time.sleep(3)
    #print("Haii...",name,"\n your rules for the game TIME PASS")
    label=Label(window,text="Haii...\n your rules for the game TIME PASS")
    time.sleep(3)
    #print("1.Guess a number in between 1 and 100 \n2.If guessed number is greater than a randomly selected number, you wil gets an output 'you are far away from the number' \n3.If guessed number is less than a randomly selected number, you wil gets an output 'you are too small from the number'\n4.If you guessed the correct number, you won the game")
    label=Label(window,text="1.Guess a number in between 1 and 100 \n2.If guessed number is greater than a randomly selected number, you wil gets an output 'you are far away from the number' \n3.If guessed number is less than a randomly selected number, you wil gets an output 'you are too small from the number'\n4.If you guessed the correct number, you won the game")
    #print("You have 10 GUESSES \n ALL THE BEST!!...Be the snake...")
    label=Label(window,text="You have 10 GUESSES \n ALL THE BEST!!...Be the snake...")
    time.sleep(3)
    count=0
    while (count<10):
        count=count+1
        guess=int(input("Enter your guess : "))
        if (guess==x):
            #print("Congragulations....\n You won",count,"try!!!")
            label=Label(window,text="Congragulations....\n You won the Game!!!")
            break
        elif (guess>x):
           # print("you are far away from the number")
           label=Label(window,text="you are far away from the number")
        elif (guess<x):
            #print("you are too small from the number")
            label=Label(window,text="you are too small from the number")
    else:
        #print("you have reached the maximum guess better luck try for next time \n The number is %d" % x)
        label=Label(window,text="you have reached the maximum guess better luck try for next time ")
    label.pack()
game()
window.mainloop()


