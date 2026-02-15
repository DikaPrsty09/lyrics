import sys
from time import sleep
import time
import os

os.system('cls')

def print_lyrics():
    lines = [
        ("Ophelia...", 0.2),
        ("Keep it one hundred on the land", 0.06),
        ("The sea", 0.06),
        ("The sky", 0.06),
        ("Pledge allegiance to your hands", 0.06),
        ("Your team", 0.06),
        ("Your vibes", 0.06),
        ("Don't care where the hell you've been", 0.05),
        ("Cause now", 0.056),
        ("You're mine", 0.056),
        ("It's 'bout to be the sleepless night", 0.054),
        ("You've been dreaming of", 0.056),
        ("The fate of Ophelia", 0.1),
    ]

    delays = [ 1, 0.4, 0.4, 0.4 , 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 1.5, 0.2 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()