import time
import sys
from pygame import mixer

print("Starting application...")
time.sleep(2)
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()

def start():
    print("Hello User. I am your narrator for today. What is your name?")
    name = input()
    print("Hello " + name + ". It is nice to meet you. Today, we will be going on a great adventure!")
    time.sleep(3)
    print("The controls for this game are simple: press the number that appears next to the choices.")
    time.sleep(3)
    
    print("Now lets dive into the story, shall we?")
    print("1: Yes \n2: No")
    num = input()
    
    #choice 1
    while True:
        if int(num) == 1:
            print("Okay, Lets Begin!")
            time.sleep(1)
            break
        elif int(num) == 2:
            print("Goodbye! :)")
            time.sleep(1)
            exit()
        else:
            print("Please enter a valid number:")
            num = input()
    
    print("Once upon a time...")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(".....")
    print("\n")

    print("Chapter 1:")
    time.sleep(3)
    print("There once was a young man named, " + name + ", who had discovered a computer for the first time.")
    time.sleep(3)
    print(name + " was so enticed by the coputer's bright lights and funny noises.")
    time.sleep(3)
    print("He immediatly grabbed onto the mouse and layed his fingers down onto the keyboard.")
    time.sleep(3)
    print("There was an intriguing icon on the desktop that caught " + name + "'s attention.")
    time.sleep(3)
    print('"Game World Online", he read to himself.')
    time.sleep(3)
    print("Does " + name + " click on the icon?")
    print("1: Yes \n2: No")
    num = input()

    #choice 2
    while True:
        if int(num) == 1:
            time.sleep(1)
            break
        elif int(num) == 2:
            print("You suddenly feel a sense of regret that you did not click on the game.")
            time.sleep(3)
            print("You walk away slow and sad.")
            time.sleep(3)
            exit()
        else:
            print("Please enter a valid number:")
            num = input()
    
    print("As you click on the game, your whole body is suddenly envoloped in bright lights.")

def choice2

start()