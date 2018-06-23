#!/usr/bin/python

# Hunter Friday
# breakcaesar.py
# Prints out all 26 possible rotations of a string you give it. Handy for CTFs!
# Usage: python breakcaesar.py "ciphertext"

import sys

if len(sys.argv) != 2:
    print "Correct usage: python breakcaesar.py \"<ciphertext>\""
    exit(1)

word = str(sys.argv[1])
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print "[*] --- Ciphertext --- [*]"
print word
print ""
print "[*] --- Solutions --- [*]"

# For each rotation:
possible_rotations = 25
for rotation in range(1, possible_rotations + 1):

    rotated = ""

    # For each letter in word:
    for i in range(0, len(word)):

        # If the letter is lowercase, rotate it
        if ord(word[i]) >= 65 and ord(word[i]) <= 90:
            index = upper_alpha.find(word[i])
            rotated += upper_alpha[(index + rotation) % len(upper_alpha)]

        # Else if the letter is upper case, rotate it
        elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
            index = lower_alpha.find(word[i])
            rotated += lower_alpha[(index + rotation) % len(lower_alpha)]

        # Else must be special character, retain it
        else:
            rotated += word[i]

    print rotated
