print("ROCK PAPER SCISSOR!")

import pyttsx3

voicecommand=str(input("Do You Want a Voice Assistant? Press 'Y' for Yes and 'N' for No:"))

if voicecommand==("Y"):
    print("This is your voice assistant")
    engine=pyttsx3.init()
    engine.say("Hello welcome to Rock Paper Scisssors with the computer, press 'R' for Rock, 'P' for Paper and 'S' for Scissor")
    engine.runAndWait()

if voicecommand==("N"):
    print("Loading..")
    
a=str(input("choose! press 'R' for Rock , press 'P' for Paper ,press 'S' for Scissor:"))

import random
list=["R","P","S"]
random_element=random.choice(list)

if a==("S") and random_element==("P") and voicecommand==("Y"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")
    engine=pyttsx3.init()
    engine.say("Congrats You Won!")
    engine.runAndWait()

if a==("S") and random_element==("P") and voicecommand==("N"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")


if a==("S") and random_element==("R") and voicecommand==("Y"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU LOST:(")
    engine=pyttsx3.init()
    engine.say("Sorry You Lost")
    engine.runAndWait()

if a==("S") and random_element==("R") and voicecommand==("N"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU LOST:(")

if a == ("R") and random_element == ("P") and voicecommand==("Y"):
    print("YOU CHOSE:", a, "COMPUTER CHOSE:", random_element)
    print("YOU LOST:(")
    engine=pyttsx3.init()
    engine.say("Sorry You Lost")
    engine.runAndWait()

if a == ("R") and random_element == ("P") and voicecommand==("N"):
    print("YOU CHOSE:", a, "COMPUTER CHOSE:", random_element)
    print("YOU LOST:(")

if a==("R") and random_element==("S") and voicecommand==("Y"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")
    engine=pyttsx3.init()
    engine.say("congrats you won")
    engine.runAndWait()

if a==("R") and random_element==("S") and voicecommand==("N"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")

if a==("P") and random_element==("R") and voicecommand==("Y"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")
    engine=pyttsx3.init()
    engine.say("Congrats You Won")
    engine.runAndWait()

if a==("P") and random_element==("R") and voicecommand==("N"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU WON!")

if a==("P") and random_element==("S") and voicecommand==("Y"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU LOST:(")
    engine=pyttsx3.init()
    engine.say("sorry you lost")
    engine.runAndWait()

if a==("P") and random_element==("S") and voicecommand==("N"):
    print("YOU CHOSE:",a,"COMPUTER CHOSE:",random_element)
    print("YOU LOST:(")

if a==random_element and voicecommand==("Y"):
    print("YOU CHOSE:", a, "COMPUTER CHOSE:", random_element)
    print("GAME DRAW!")
    engine=pyttsx3.init()
    engine.say("Game Drawn")
    engine.runAndWait()
    
if a==random_element and voicecommand==("N"):
    print("YOU CHOSE:", a, "COMPUTER CHOSE:", random_element)
    print("GAME DRAW!")

#CODE ENDS HERE
