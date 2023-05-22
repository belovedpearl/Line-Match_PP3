# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet


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



def print_match(columns):
    """
     Inverts the columns into a 5 by 5 matrix
     Prints out the match
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def get_match_set(rows, cols, rep):
    """
     Create a list from the set object
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
        line_point = input("How many points will you like to start with (Amount is multiplied by the number of lines you choose\n)?")
        if line_point.isdigit():
            line_point = int(line_point)
            if MIN_BET <= line_point <= MAX_BET:
                break
            else:
                print(f"Total worth must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return amount

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
            if 1 <= guess_lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines to continue")
        else:
            print("Please enter a number")
    return guess_lines



def generate_match(point):
    """
     Generate the 5 X 5 number combination
    """
    lines = get_number_of_lines()
    print(lines)
    while True:
       point_assigned = assign_point()
       total_point = point_assigned * lines
       if total_point > points:
           print(f"You do not have enough to points for that game, your current balance is  {points}")
       else:
           break
    print(f"You are adding {point_assigned} for {lines} lines. Total guess is equal to  {total_point}")
    match_set = get_match_set(ROWS, COLS, symbol_count)
    print_match(match_set)
    winnings, winning_lines = check_winnings(match_set, lines, point_assigned, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines", *winning_lines)
    return winnings - total_point

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
        generate_match(points)
   


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