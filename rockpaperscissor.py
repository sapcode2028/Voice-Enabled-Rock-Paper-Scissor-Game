import pyttsx3
import random

def speak(text, voicecommand, engine):
    if voicecommand == "Y" and engine:
        engine.say(text)
        engine.runAndWait()

def play_game():
    print("ROCK PAPER SCISSOR!")

    voicecommand = input("Do You Want a Voice Assistant? Press 'Y' for Yes and 'N' for No: ").strip().upper()

    engine = None
    if voicecommand == "Y":
        print("This is your voice assistant")
        engine = pyttsx3.init()
        engine.say("Hello! Welcome to Rock Paper Scissors with the computer. Press 'R' for Rock, 'P' for Paper, and 'S' for Scissors.")
        engine.runAndWait()
    else:
        print("Loading...")

    a = input("Choose! Press 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").strip().upper()
    if a not in ["R", "P", "S"]:
        print("Invalid input. Please enter R, P, or S.")
        speak("Invalid input. Please enter R, P, or S.", voicecommand, engine)
        return

    computer_choice = random.choice(["R", "P", "S"])

    print("YOU CHOSE:", a, "| COMPUTER CHOSE:", computer_choice)

    if a == computer_choice:
        print("GAME DRAW!")
        speak("Game Drawn", voicecommand, engine)
    elif (a == "R" and computer_choice == "S") or \
         (a == "P" and computer_choice == "R") or \
         (a == "S" and computer_choice == "P"):
        print("YOU WON!")
        speak("Congrats! You won.", voicecommand, engine)
    else:
        print("YOU LOST :(")
        speak("Sorry, you lost.", voicecommand, engine)

    play_again = input("Do you want to play again? Press 'Y' for Yes and 'N' for No: ").strip().upper()
    if play_again == "Y":
        play_game()
    else:
        print("Thanks for playing!")
        speak("Thanks for playing!", voicecommand, engine)

play_game()

