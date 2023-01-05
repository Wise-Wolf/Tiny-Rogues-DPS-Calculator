import sys
import os

def delete_last_line():
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def overwrite_line():
    sys.stdout.write("\033[F")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')