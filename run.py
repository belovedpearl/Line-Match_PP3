# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet

name = ""   # Global variable declared to be changed with each user

def welcome_text():
    """
     Displays the title of the game
    """
    print(pyfiglet.figlet_format("LINE MATCH", font="starwars", justify="center", width=110))



def main():
    welcome_text()
    print()
    print()
    print("Welcome to the game...")
    global name
    name = input("Enter your name: ")
    


main()
print(name)