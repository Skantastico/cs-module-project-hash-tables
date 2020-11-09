# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import os.path

input = os.path.join(os.path.dirname(__file__), 'ciphertext.txt')

with open(input) as f:
    ciphertext = f.read()

def count_letters(s):
    dict = {}
    letters = [l.upper() for l in s if l.isalpha()]
    for letter in letters:
        dict[letter] = dict[letter] + 1 if letter in dict else 1
    return dict

def caesarkey(ciphertext):
    letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    sorted_letters = sorted(count_letters(ciphertext).items(), key=lambda x: x[1], reverse=True)
    key = {}

    for (i, l) in enumerate(sorted_letters):
        key[l[0]] = letters[i]

    return key

def crack_text(ciphertext):
    key = caesarkey(ciphertext)
    decoded = ""

    for c in ciphertext:
        decoded += key[c] if c in key else c
    print(decoded)


crack_text(ciphertext)
