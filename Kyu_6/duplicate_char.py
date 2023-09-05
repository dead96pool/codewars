"""
link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
"""
from collections import Counter

def dup_char(string):
    dup = 0
    # making a dict object from the characters in the string
    str_dict = dict(Counter(string.lower()))
    
    # checking the count of repeated characters
    for char in str_dict.keys():
        if str_dict[char] > 1:
            dup += 1
    
    return dup


# count all instances in the string and remove them
    

print(dup_char("indivisibility"))
print(dup_char("Indivisibilities"))
print(dup_char("abcdeaB"))