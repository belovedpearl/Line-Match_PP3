# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet

name = ""   # Global variable declared to be changed with each user

def choose_points():
    """
      Allows user to choose points in number
      Checks if an actual number was chosen
      Continues to ask until the right thing is entered
    """
    print("Choose your starting point.")

    while True:
        points = input("How many points will you like to start with?\n")
        if points.isdigit():
            points = int(points)
            if points > 0:
                break
            else:
                print("Points must be greater than zero")
        else:
            print("Please enter a number")
    return points

def open_game():
    """
    Opens up the game to the user
    """
    points = choose_points()
    print()
    print(f"You have chosen a starting point of {points}")
    
    while True:
        print(f"Current balance is {points} points.")
        generate_match()
   


def instruct():
    print("To start the game, pick your desired starting points.\n")
    print("Computer randomly creates a 5 x 5 grid of alphabets, you are to guess what row is/are likely to contain the same set of alphabet\n")
    print("To guess, choose between 1-5.\n")
    print("Commit some points to each lines.\n")
    print("Press enter to play the game till you have no more or less points to continue.\n")
    print("Your game starts here...\n")
    open_game()

def new_game(name):
    """
       Opens up the instruction and the game section
    """
    print(f"Welcome {name}, choose from the option below...\n")
    decision = input("Press i to view instruction. \nPress n to play new game\n")
    if decision == "i":
        instruct()
    elif decision == "n":
        open_game()
    else:
        print("You have not chosen a valid option.\n")

def welcome_text():
    """
      Displays the title of the game
    """
    print(pyfiglet.figlet_format("LINE MATCH", font="starwars", justify="center", width=110))


def main():
    """
      Defines the main function
    """
    welcome_text()
    print()
    print()
    print("Welcome to the game...")
    global name
    name = input("Enter your name: ")
    while True:
        new_game_decision = input('Press y to start the game\n or \n Press n to quit:\n')
        if new_game_decision == 'y':
            new_game(name)
            break
        elif new_game_decision == 'n':
            main()
            break
        else:
            print('Please enter either y or n')

main()
print(name)