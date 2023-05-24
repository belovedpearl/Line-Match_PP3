import sys
import time
import os

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

