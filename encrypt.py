# Use this code for the LCHS Web Form project (Part 2).

import string

def alphabet_position(char):
    return string.ascii_lowercase.find(char.lower())

def shift_character(char, shift):
    if char.lower() not in string.ascii_lowercase:
        return char
    new_index = (alphabet_position(char) + shift)%26
    new_char = string.ascii_lowercase[new_index]
    if char.isupper():
        return new_char.upper()
    else:
        return new_char

def encrypt_with_shift(text, shift):
    new_message = ''
    for char in text:
        new_message += shift_character(char, shift)
    return new_message
