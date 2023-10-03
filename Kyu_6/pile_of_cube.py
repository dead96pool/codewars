"""
Build a pile of cubes
link: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python
"""

def find_nb(m):
    # using the sum of n cubic numbers is (n(n+1)/2)^2
    # for large numbers n(n+1) = 2(sum^0.5) ~= n^2 
    # approx val of n 
    n = int((2 * m ** 0.5) ** 0.5)
    if (n * (n + 1) // 2)**2 == m:
        return n
    else:
        return -1

print(find_nb(4183059834009))   #2022