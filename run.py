# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet
import random
from set import *



# Constant variables to be used for the game
MAX_LINES = 5
MAX_POINTS = 100
MIN_POINTS = 1

ROWS = 5
COLS = 5

symbol_count = {
    "W": 2,
    "X": 4,
    "Y": 6,
    "Z": 8
}

symbol_value = {
    "W": 5,
    "X": 4,
    "Y": 3,
    "Z": 2
}


name = ""   # Global variable declared to be changed with each user

def check_winnings(columns, lines, guess, values):
    winning_lines = []
    win = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check  = column[line]
            if symbol != symbol_check:
                break
        else:
            win += values[symbol] * guess 
            winning_lines.append(line + 1)
    return win, winning_lines


def print_match(columns):
    """
     Inverts the columns into a 5 by 5 matrix
     Prints out the match
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row].center(10), end=" | ")
            else:
                print(column[row].center(10), end="")
        print()

def get_match_set(rows, cols, rep):
    """
     Create a list from the object listed as constant
    """
    # Create an empty list to take in the loop
    all_rep = []
    for rep, rep_count in rep.items():
        for i in range(rep_count):
            all_rep.append(rep)
    
    columns = []
    for col in range(cols):
        column = []
        current_rep = all_rep[:]  # Creates a similar list in all_rep
        for row in range(rows):
            value = random.choice(current_rep)
            current_rep.remove(value) # Values removed to avoid repetition
            column.append(value)
            
        columns.append(column)
        
    return columns


def assign_point():
    """
      Allow user to choose how many points will be used in playing
      validates that a number was inputed
    """
    while True:
        line_point = input("How many points will you like to start with (Your point is multiplied by the number of lines choosen)?\n")
        if line_point.isdigit():
            line_point = int(line_point)
            if  line_point >= MIN_POINTS and line_point <= MAX_POINTS:
                break
            else:
                typewriter(f"Total worth of points must be between {MIN_POINTS} and {MAX_POINTS}")
        else:
            typewriter("Please enter a number")
    return line_point


def get_number_of_lines():
    """
      Allows user to choose number of lines to guess
      Checks if an actual number was chosen
      Continues to ask until the right thing is entered
    """
    
    while True:
        guess_lines = input("Enter the number of lines to guess (1-" + str(MAX_LINES) + "): ")
        if guess_lines.isdigit():
            guess_lines = int(guess_lines)
            if guess_lines >= 1 and guess_lines <= MAX_LINES:
                break
            else:
                typewriter("Enter a valid number between 1-5 to continue")
        else:
            typewriter("Please enter a number")
    return guess_lines



def generate_match(point):
    """
     Generate the 5 X 5 number combination
    """
    lines = get_number_of_lines()
    
    while True:
       point_assigned = assign_point()
       total_point = point_assigned * lines
       if total_point > point:
           print(f"You do not have enough to points for that game, your current balance is  {point}")
           
       else:
           break
    print(f"You are adding {point_assigned} for {lines} lines. Total guess is equal to  {total_point}")
    match_set = get_match_set(ROWS, COLS, symbol_count)
    print_match(match_set)
    win, winning_lines = check_winnings(match_set, lines, point_assigned, symbol_value)
    if win >= 1:
        typewriter(f"You guess {win} lines right.\n")
        typewriter(f"You had the right guess for lines," *winning_lines)
    else:
        typewriter("Your guess was wrong.\n")
    return win - total_point


def choose_points():
    """
      Allows user to choose points in number
      Checks if an actual number was chosen
      Continues to ask until the right thing is entered
    """
    typewriter("Choose your starting point.\n")

    while True:
        points = input("How many points will you like to start with? ")
        if points.isdigit():
            points = int(points)
            if points > 0 and points <= MAX_POINTS:
                break
            else:
                typewriter(f"To play this game, your points must be greater than 0 and less than OR equal to {MAX_POINTS}")
        else:
            typewriter("Please enter a number")
    return points


def open_game():
    """
    Opens up the game to the user
    """
    points = choose_points()
    print()
    typewriter(f"You have chosen a starting point of {points}\n")
    
    while True:
        typewriter(f"Current balance is {points} points.\n")
        if points == 0:
            typewriter(f"{name}, You are out of point, restart to play again!!!")
            break
        answer = input("Press p to play or q to quit.\n")
        if answer == "q":
            break
        elif answer == "p":
            points += generate_match(points)
    clear_screen()
    typewriter(f"You left the game, {points} points left!\n")
        
        

def instruct():
    typewriter("To start the game, pick your desired starting points.\n")
    typewriter("Computer randomly creates a 5 x 5 grid of alphabets.\n")
    typewriter("You are to guess what row is or are likely to contain the same set of alphabet\n")
    print()
    typewriter("To guess, choose between 1-5:\n")
    typewriter("Choose 1 to guess the first line.\n")
    typewriter("Choose 2 to guess the first two lines.\n")
    typewriter("Choose 3 to guess the first  three lines.\n")
    typewriter("Choose 4 to guess the first four lines.\n")
    typewriter("Choose 5 to guess all five lines.\n")
    print()
    typewriter("Commit some points to each lines.\n")
    print()
    typewriter("Press enter to play the game till you have no more or less points to continue.\n")
    print()
    clear_screen()
    typewriter("Your game starts here...\n")
    clear_screen()
    open_game()


def new_game(name):
    """
       Opens up the instruction and links to the game section
    """
    typewriter(f"Welcome {name}, choose from the option below...\n")
    print()
    decision = input("Press i to view instruction.\nPress n to play new game\n")
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
    typewriter("Welcome to the game...\n")
    global name
    name = input("Enter your name: ")
    while True:
        new_game_decision = input("Press y to start the game\n or \nPress n to quit:\n")
        if new_game_decision == "y":
            new_game(name)
            break
        elif new_game_decision == "n":
            main()
            break
        else:
            print("Please enter either y or n")


main()


