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

    while True:
        if int(num) == 1:
            print("Okay, Lets Begin!")
            time.sleep(1)
            break
        elif int(num) == 2:
            exit()
        else:
            print("Please enter a valid number:")
            num = input()
    
    print("Once upon a time...")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(".....")

    print("")

start()