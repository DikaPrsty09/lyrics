import sys
from time import sleep
import time
import os

os.system('cls')

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def print_lyrics():
    lines = [
        ("Everything that you've ever dreamed of", 0.07),
        ("Disappearing when you wake up", 0.088),
        ("But there's nothing to be", 0.076),
        ("Afraid of", 0.09),
        ("Even when the night", 0.076),
        ("Changes", 0.08),
        ("It will never change", 0.076), 
        ("Baby", 0.08),
        ("It will never change", 0.076), 
        ("Baby", 0.08),
        ("It will never change", 0.076), 
        ("Me and you", 0.12),
    ]

    delays = [ 0.6, 0.7, 0.2 , 0.6, 0.6, 1, 0.6, 0.9, 0.6, 0.9, 0.9, 0.9 ]


    hide_cursor()
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()