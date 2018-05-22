#!/usr/bin/env python3
"""
A Caesar ciper encoder and decoder
"""

MESSAGE = 'five pm lingampally station'
SHIFT = 22
CODE = ''

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'

"""
Encode
"""
for letter in MESSAGE:
    c = 0
    while letter != ALPHABET[c]:
        c += 1
    CODE = CODE + ALPHABET[(c+SHIFT) % len(ALPHABET)]

print(CODE)
