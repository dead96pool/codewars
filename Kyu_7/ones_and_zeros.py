"""
link: https://www.codewars.com/kata/578553c3a1b8d5c40300037c/python
"""

def binary_array_to_number(array):
    return sum([num*(2**(len(array)-1-idx)) for idx, num in enumerate(array)])




# decimal number 6 = 0 1 1 0
array = [0, 1, 0, 1]
print(binary_array_to_number(array))