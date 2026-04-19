import sys
from time import sleep
import time
import os

BLUE = "\033[1;96m"   
RESET = "\033[0m"

def hide_cursor():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def print_lyrics():
    lines = [
        ("But you'll never be alone ", 0.07),
        ("I'll be with you from dusk 'til dawn ", 0.07),
        ("I'll be with you from dusk 'til dawn ", 0.07),
        ("Baby, I'm right here ", 0.08),
        ("I'll hold you when things go wrong ", 0.07),
        ("I'll be with you from dusk 'til dawn ", 0.07),
        ("I'll be with you from dusk 'til dawn ", 0.07), 
        ("Baby, I'm right here ", 0.08), 
    ]

    delays = [0.4, 0.1, 0.2, 0.8, 0.4, 0.1, 0.2, 0.4]

    hide_cursor()

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(BLUE + char + RESET, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

    print("\n")

    time.sleep(3)

    show_cursor()

print_lyrics()