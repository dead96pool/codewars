"""
link: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
"""

def comp(arr1, arr2):
    if arr1 == None or arr2 == None:
        return False
    elif len(arr1) != len(arr2):
        return False
    else:
        return sorted([num**2 for num in arr1]) == sorted(arr2)
    
def assert_equals(output, result):
    print(output == result)

if __name__ == "__main__":
    
    a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert_equals(comp(a1, a2), True)
