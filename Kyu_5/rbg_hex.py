"""
link: https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""

def fix_range(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def rgb(r, g, b):
    hex_str = ""
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    hex_str = f"{r:02X}{g:02X}{b:02X}"
    return hex_str




def assert_equals(output, expected):
    print(output == expected)

#assert_equals(rgb(0, 0, 0), "000000") # "testing zero values")
#assert_equals(rgb(1, 2, 3), "010203") # "testing near zero values")
#assert_equals(rgb(255, 255, 255), "FFFFFF") # "testing max values")
#assert_equals(rgb(254, 253, 252), "FEFDFC") # "testing near max values")
assert_equals(rgb(-20, 275, 125), "00FF7D") # "testing out of range values")