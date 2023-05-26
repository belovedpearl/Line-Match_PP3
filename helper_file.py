import sys
import time
import os

# os.system("cls")
# """ ANSI color codes """
# COLORS = {\
#     "black": "\033[0;30m",
#     "red": "\033[0;31m",
#     "green": "\033[0;32m",
#     "brown": "\033[0;33m",
#     "blue": "\033[0;34m",
#     "purple": "\033[0;35m",
#     "cyan": "\033[0;36m",
#     "cyan-background": "\001[46;1m",
#     "black_background": "\u001b[40m",
# }
# def colorRep(text):
#     for color in COLORS:
#         text = text.replace("[[" + color + "]]",COLORS[color])
#     return text

# def print_art(text):
#     f = open("title_art.txt","r")
#     ascii = "".join(f.readlines())
#     print(colorRep(ascii))

def typewriter(message):
    """
    Writes the message in a typewriter format where used
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

def clear_screen():
    os.system("clear")
    