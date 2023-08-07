"""
link: https://www.codewars.com/kata/523f5d21c841566fde000009/python
"""

def array_diff(a, b):
    return [num for num in a if num not in b]
    

if __name__ == "__main__":
    arr_a = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
    arr_b = [1, 2, 3, 4]
    print(array_diff(arr_a, arr_b))