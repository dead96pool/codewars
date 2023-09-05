"""
link: https://www.codewars.com/kata/530e15517bc88ac656000716
"""

def rot_13(message):
    cipher = ""
    for char in message:
        if char.isupper():
            cipher += chr( (ord(char) + 13 - 65) % 26 + 65 )
        elif char.islower():
            cipher += chr( (ord(char) + 13 - 97) % 26 + 97 )
        else:
            cipher += char
    return cipher



print(rot_13("aA bB zZ 1234 *!?%"))
